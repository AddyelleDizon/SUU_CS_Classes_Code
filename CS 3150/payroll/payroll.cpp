#include "payroll.h"
#include <iomanip>
#include <algorithm>

// base class: employee functions
Employee::Employee(int id, const std::string& first, const std::string& last)
    : employee_id(id), first_name(first), last_name(last) {}

int Employee::get_id() const {
    return employee_id; 
}

std::string Employee::get_first() const { 
    return first_name; 
}

std::string Employee::get_last() const { 
    return last_name; 
}

std::ostream& operator<<(std::ostream& os, const Employee& e) {
    e.print(os);
    return os;
}

// sub-class: full time employee functions; i forgot how to do it in a better way, cant view meeting recordings
FullTimeEmployee::FullTimeEmployee(int id, const std::string& first, const std::string& last, double salary, double bonus, const std::vector<std::string>& benefits)
    : Employee(id, first, last), salary_(salary), bonus_(bonus) {

    for (const auto& b : benefits) {
        if (std::find(VALID_BENEFITS.begin(), VALID_BENEFITS.end(), b) != VALID_BENEFITS.end())
            benefits_.push_back(b);
    }
}

double FullTimeEmployee::get_salary() const { 
    return salary_; 
}
void FullTimeEmployee::set_salary(double s) { 
    salary_ = s; 
}

double FullTimeEmployee::get_bonus() const { 
    return bonus_; 
}

void FullTimeEmployee::set_bonus(double b) { 
    bonus_ = b; 
}

double FullTimeEmployee::get_401k() const { 
    return salary_ * 0.05; 
}

std::vector<std::string> FullTimeEmployee::get_benefits() const { 
    return benefits_; 
}

void FullTimeEmployee::set_benefits(const std::vector<std::string>& b) { 
    benefits_ = b; 
}

double FullTimeEmployee::pay() const { 
    return salary_ + bonus_; 
}

std::string FullTimeEmployee::get_type() const { 
    return "FULL TIME"; 
}

void FullTimeEmployee::print(std::ostream& os) const {
    os << last_name << ", " << first_name << ": FULL TIME\n";
    os << "Salary: $" << salary_ << "\n";
    os << "Bonus: $" << bonus_ << "\n";
    os << "Benefits: ";
    if (benefits_.empty()) os << "NONE";
    else {
        for (size_t i = 0; i < benefits_.size(); ++i) {
            os << benefits_[i];
            if (i < benefits_.size() - 1) os << ", ";
        }
    }
    os << "\n";
}

// sub-class: part time employee
PartTimeEmployee::PartTimeEmployee(int id, const std::string& first, const std::string& last, double wage, double hours, double sick_time)
    : Employee(id, first, last), wage_(wage), hours_worked_(hours), sick_time_(sick_time) {}

double PartTimeEmployee::get_wage() const { 
    return wage_; 
}

void PartTimeEmployee::set_wage(double w) { 
    wage_ = w; 
}

double PartTimeEmployee::get_hours() const { 
    return hours_worked_; 
}

void PartTimeEmployee::set_hours(double h) { 
    hours_worked_ = h; 
}

double PartTimeEmployee::get_sick_time() const { 
    return sick_time_; 
}

void PartTimeEmployee::set_sick_time(double s) { 
    sick_time_ = s; 
}

double PartTimeEmployee::pay() const { 
    return wage_ * hours_worked_; 
}

std::string PartTimeEmployee::get_type() const { 
    return "PART TIME"; 
}

void PartTimeEmployee::print(std::ostream& os) const {
    os << last_name << ", " << first_name << ": PART TIME\n";
    os << "Wage: $" << wage_ << "/hour\n";
    os << "Hours Worked: " << hours_worked_ << "\n";
    os << "Sick Time Accrued: " << sick_time_ << " hours\n";
}