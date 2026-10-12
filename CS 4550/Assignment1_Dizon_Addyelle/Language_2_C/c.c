#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct {
    int id;
    char product[256];
    char category[256];
    int qty;
    double price;
    double value;
} Record;

typedef struct {
    int line_num;
    char reason[256];
} InvalidRecord;

typedef struct {
    char category[256];
    double total;
} CategoryTotal;

char* trim(char* s) {
    while (isspace((unsigned char)*s)) s++;
    if (*s == 0) return s;
    char* end = s + strlen(s) - 1;
    while (end > s && isspace((unsigned char)*end)) end--;
    end[1] = '\0';
    return s;
}

bool check_decimals(const char* s) {
    const char* dot = strchr(s, '.');
    if (!dot) return true;
    return strlen(dot + 1) <= 2;
}

bool file_exists(const char* path) {
    FILE* f = fopen(path, "r");
    if (f) {
        fclose(f);
        return true;
    }
    return false;
}

void get_dir_path(const char* full_path, char* dir_out) {
    strcpy(dir_out, full_path);
    char* last_slash = strrchr(dir_out, '/');
    char* last_bslash = strrchr(dir_out, '\\');
    char* sep = last_slash > last_bslash ? last_slash : last_bslash;
    if (sep) {
        *sep = '\0';
    } else {
        strcpy(dir_out, ".");
    }
}

void write_zero_results(const char* report_path, const char* errors_path) {
    FILE* rFile = fopen(report_path, "w");
    if (rFile) {
        fprintf(rFile, "Valid transactions: 0\nInvalid transactions: 0\nTotal revenue: 0.00\nHighest-value transaction: N/A\n");
        fclose(rFile);
    }
    FILE* eFile = fopen(errors_path, "w");
    if (eFile) {
        fprintf(eFile, "No invalid records\n");
        fclose(eFile);
    }
}

int compare_records(const void* a, const void* b) {
    const Record* r1 = (const Record*)a;
    const Record* r2 = (const Record*)b;
    if (r1->value > r2->value) return -1;
    if (r1->value < r2->value) return 1;
    return r1->id - r2->id;
}

int compare_categories(const void* a, const void* b) {
    const CategoryTotal* c1 = (const CategoryTotal*)a;
    const CategoryTotal* c2 = (const CategoryTotal*)b;
    return strcmp(c1->category, c2->category);
}

int split_csv_line(char* line, char fields[5][256]) {
    int field_count = 0;
    char* start = line;
    char* ptr = line;

    while (*ptr != '\0') {
        if (*ptr == '\n' || *ptr == '\r') {
            *ptr = '\0';
            break;
        }
        if (*ptr == ',') {
            *ptr = '\0';
            if (field_count < 5) {
                strncpy(fields[field_count], start, 255);
                fields[field_count][255] = '\0';
            }
            field_count++;
            start = ptr + 1;
        }
        ptr++;
    }

    if (field_count < 5) {
        strncpy(fields[field_count], start, 255);
        fields[field_count][255] = '\0';
    }
    field_count++;

    return field_count;
}

int main(int argc, char* argv[]) {
    char exe_dir[1024];
    get_dir_path(argv[0], exe_dir);

    char candidate_paths[6][1024];
    snprintf(candidate_paths[0], sizeof(candidate_paths[0]), "input/transactions.csv");
    snprintf(candidate_paths[1], sizeof(candidate_paths[1]), "../input/transactions.csv");
    snprintf(candidate_paths[2], sizeof(candidate_paths[2]), "%s/input/transactions.csv", exe_dir);
    snprintf(candidate_paths[3], sizeof(candidate_paths[3]), "%s/../input/transactions.csv", exe_dir);
    snprintf(candidate_paths[4], sizeof(candidate_paths[4]), "%s/../../input/transactions.csv", exe_dir);
    snprintf(candidate_paths[5], sizeof(candidate_paths[5]), "transactions.csv");

    char csv_path[1024] = "";
    for (int i = 0; i < 6; i++) {
        if (file_exists(candidate_paths[i])) {
            strcpy(csv_path, candidate_paths[i]);
            break;
        }
    }

    char report_path[1024];
    char errors_path[1024];
    snprintf(report_path, sizeof(report_path), "%s/report.txt", exe_dir);
    snprintf(errors_path, sizeof(errors_path), "%s/errors.txt", exe_dir);

    if (strlen(csv_path) == 0) {
        printf("Error: transactions.csv not found in candidate input folders.\n");
        return 1;
    }

    FILE* file = fopen(csv_path, "r");
    if (!file) {
        printf("Error: transactions.csv could not be opened at %s\n", csv_path);
        return 1;
    }

    char line_buffer[1024];
    if (!fgets(line_buffer, sizeof(line_buffer), file)) {
        fclose(file);
        write_zero_results(report_path, errors_path);
        return 1;
    }

    char* trimmed_header = trim(line_buffer);
    if (strcmp(trimmed_header, "transaction_id,product_name,category,quantity,unit_price") != 0) {
        printf("Error: Fatal header error.\n");
        fclose(file);
        return 1;
    }

    Record* valid_records = NULL;
    size_t valid_count = 0;
    size_t valid_cap = 0;

    InvalidRecord* invalid_records = NULL;
    size_t invalid_count = 0;
    size_t invalid_cap = 0;

    int* seen_ids = NULL;
    size_t seen_count = 0;
    size_t seen_cap = 0;

    int line_idx = 2;

    while (fgets(line_buffer, sizeof(line_buffer), file)) {
        char fields[5][256];
        int field_count = split_csv_line(line_buffer, fields);

        if (field_count != 5) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Does not contain exactly 5 fields");
            invalid_count++;
            line_idx++;
            continue;
        }

        char* f_id = trim(fields[0]);
        char* f_prod = trim(fields[1]);
        char* f_cat = trim(fields[2]);
        char* f_qty = trim(fields[3]);
        char* f_price = trim(fields[4]);

        char* endptr;
        long t_id_long = strtol(f_id, &endptr, 10);
        if (*f_id == '\0' || *endptr != '\0' || t_id_long <= 0) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Transaction ID must be a positive integer");
            invalid_count++;
            line_idx++;
            continue;
        }
        int t_id = (int)t_id_long;

        bool duplicate = false;
        for (size_t i = 0; i < seen_count; i++) {
            if (seen_ids[i] == t_id) {
                duplicate = true;
                break;
            }
        }
        if (duplicate) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Duplicate transaction ID");
            invalid_count++;
            line_idx++;
            continue;
        }

        if (strlen(f_prod) == 0) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Product name cannot be empty");
            invalid_count++;
            line_idx++;
            continue;
        }

        if (strlen(f_cat) == 0) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Category cannot be empty");
            invalid_count++;
            line_idx++;
            continue;
        }

        long qty_long = strtol(f_qty, &endptr, 10);
        if (*f_qty == '\0' || *endptr != '\0' || qty_long <= 0) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Quantity must be a positive integer");
            invalid_count++;
            line_idx++;
            continue;
        }
        int qty = (int)qty_long;

        double price = strtod(f_price, &endptr);
        if (*f_price == '\0' || *endptr != '\0' || price < 0.0 || !check_decimals(f_price)) {
            if (invalid_count >= invalid_cap) {
                invalid_cap = invalid_cap == 0 ? 16 : invalid_cap * 2;
                invalid_records = realloc(invalid_records, invalid_cap * sizeof(InvalidRecord));
            }
            invalid_records[invalid_count].line_num = line_idx;
            strcpy(invalid_records[invalid_count].reason, "Unit price must be >= 0.00 with max 2 decimals");
            invalid_count++;
            line_idx++;
            continue;
        }

        if (seen_count >= seen_cap) {
            seen_cap = seen_cap == 0 ? 16 : seen_cap * 2;
            seen_ids = realloc(seen_ids, seen_cap * sizeof(int));
        }
        seen_ids[seen_count++] = t_id;

        if (valid_count >= valid_cap) {
            valid_cap = valid_cap == 0 ? 16 : valid_cap * 2;
            valid_records = realloc(valid_records, valid_cap * sizeof(Record));
        }

        valid_records[valid_count].id = t_id;
        strcpy(valid_records[valid_count].product, f_prod);
        strcpy(valid_records[valid_count].category, f_cat);
        valid_records[valid_count].qty = qty;
        valid_records[valid_count].price = price;
        valid_records[valid_count].value = qty * price;
        valid_count++;

        line_idx++;
    }
    fclose(file);

    FILE* rFile = fopen(report_path, "w");
    FILE* eFile = fopen(errors_path, "w");

    if (valid_count == 0) {
        if (rFile) {
            fprintf(rFile, "Valid transactions: 0\nInvalid transactions: %zu\nTotal revenue: 0.00\nHighest-value transaction: N/A\n", invalid_count);
        }
    } else {
        double total_revenue = 0.0;
        Record* highest = &valid_records[0];

        CategoryTotal* cat_totals = NULL;
        size_t cat_count = 0;
        size_t cat_cap = 0;

        for (size_t i = 0; i < valid_count; i++) {
            total_revenue += valid_records[i].value;

            if (valid_records[i].value > highest->value ||
               (valid_records[i].value == highest->value && valid_records[i].id < highest->id)) {
                highest = &valid_records[i];
            }

            int cat_idx = -1;
            for (size_t j = 0; j < cat_count; j++) {
                if (strcmp(cat_totals[j].category, valid_records[i].category) == 0) {
                    cat_idx = (int)j;
                    break;
                }
            }

            if (cat_idx >= 0) {
                cat_totals[cat_idx].total += valid_records[i].value;
            } else {
                if (cat_count >= cat_cap) {
                    cat_cap = cat_cap == 0 ? 16 : cat_cap * 2;
                    cat_totals = realloc(cat_totals, cat_cap * sizeof(CategoryTotal));
                }
                strcpy(cat_totals[cat_count].category, valid_records[i].category);
                cat_totals[cat_count].total = valid_records[i].value;
                cat_count++;
            }
        }

        qsort(cat_totals, cat_count, sizeof(CategoryTotal), compare_categories);
        qsort(valid_records, valid_count, sizeof(Record), compare_records);

        if (rFile) {
            fprintf(rFile, "Valid transactions: %zu\n", valid_count);
            fprintf(rFile, "Invalid transactions: %zu\n", invalid_count);
            fprintf(rFile, "Total revenue: %.2f\n", total_revenue);
            fprintf(rFile, "Highest-value transaction: ID %d, %s, %s, Qty %d, Price %.2f, Value %.2f\n\nCategory Totals:\n",
                    highest->id, highest->product, highest->category, highest->qty, highest->price, highest->value);

            for (size_t i = 0; i < cat_count; i++) {
                fprintf(rFile, "%s: %.2f\n", cat_totals[i].category, cat_totals[i].total);
            }

            fprintf(rFile, "\nSorted Transactions:\n");
            for (size_t i = 0; i < valid_count; i++) {
                fprintf(rFile, "%d,%s,%s,%d,%.2f,%.2f\n",
                        valid_records[i].id, valid_records[i].product, valid_records[i].category,
                        valid_records[i].qty, valid_records[i].price, valid_records[i].value);
            }
        }
        free(cat_totals);
    }

    if (eFile) {
        if (invalid_count == 0) {
            fprintf(eFile, "No invalid records\n");
        } else {
            for (size_t i = 0; i < invalid_count; i++) {
                fprintf(eFile, "Line %d: %s\n", invalid_records[i].line_num, invalid_records[i].reason);
            }
        }
    }

    if (rFile) fclose(rFile);
    if (eFile) fclose(eFile);

    if (valid_count > 0) {
        char input_buf[256];
        int lookup_id = 0;

        while (1) {
            printf("Enter a positive integer Transaction ID for lookup: ");
            if (scanf("%255s", input_buf) == 1) {
                char* endptr;
                long parsed = strtol(input_buf, &endptr, 10);
                if (*input_buf != '\0' && *endptr == '\0' && parsed > 0) {
                    lookup_id = (int)parsed;
                    break;
                }
            }
            printf("Invalid input. Must be a positive integer.\n");
        }

        bool found = false;
        for (size_t i = 0; i < valid_count; i++) {
            if (valid_records[i].id == lookup_id) {
                printf("Found: ID %d, %s, %s, Qty %d, Price %.2f, Value %.2f\n",
                       valid_records[i].id, valid_records[i].product, valid_records[i].category,
                       valid_records[i].qty, valid_records[i].price, valid_records[i].value);
                found = true;
                break;
            }
        }

        if (!found) {
            printf("Transaction ID %d does not exist among valid records.\n", lookup_id);
        }
    } else {
        printf("No valid transactions available for lookup.\n");
    }

    free(valid_records);
    free(invalid_records);
    free(seen_ids);

    return 0;
}