#ifndef payroll_h
#define payroll_h

#include <string>
#include <vector>
#include <iostream>

// benefits
static const std::vector<std::string> VALID_BENEFITS = {
    "medical",
    "dental",
    "vision",
    "life insurance",
    "disability"
};

// base class: employee
class Employee {
    public:
        Employee(int id, const std::string& first, const std::string& last);
        virtual ~Employee() = default;

        int get_id() const;
        std::string get_first() const;
        std::string get_last() const;

        virtual double pay() const = 0;
        virtual std::string get_type() const = 0;

        virtual void print(std::ostream& os) const = 0;
        friend std::ostream& operator<<(std::ostream& os, const Employee& e);

    protected:
        int employee_id;
        std::string first_name;
        std::string last_name;
};

// sub-class: full time employee
class FullTimeEmployee : public Employee {
    public:
        FullTimeEmployee(int id, const std::string& first, const std::string& last,
                        double salary, double bonus,
                        const std::vector<std::string>& benefits);

        double get_salary() const;
        void set_salary(double s);

        double get_bonus() const;
        void set_bonus(double b);

        double get_401k() const;

        std::vector<std::string> get_benefits() const;
        void set_benefits(const std::vector<std::string>& b);

        double pay() const override;
        std::string get_type() const override;

        void print(std::ostream& os) const override;

    private:
        double salary_;
        double bonus_;
        std::vector<std::string> benefits_;
};

// sub-class: part time employee
class PartTimeEmployee : public Employee {
    public:
        PartTimeEmployee(int id, const std::string& first, const std::string& last,
                        double wage, double hours, double sick_time);

        double get_wage() const;
        void set_wage(double w);

        double get_hours() const;
        void set_hours(double h);

        double get_sick_time() const;
        void set_sick_time(double s);

        double pay() const override;
        std::string get_type() const override;

        void print(std::ostream& os) const override;

    private:
        double wage_;
        double hours_worked_;
        double sick_time_;
};

#endif