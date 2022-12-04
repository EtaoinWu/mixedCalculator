class Calculator:
    def __init__(self):
        pass

    def fmt_num(self, v):
        s = f"{v:.10f}"
        while s[-1] == "0":
            s = s[:-1]
        if s[-1] == ".":
            s = s[:-1]
        if s == "-0":
            s = "0"
        if len(s) > 16:
            s = s[:16]
        return s

    def __call__(self, s):
        for c in s:
            if c not in "0123456789+-*/%()":
                return "Error"
        s = s.replace("×", "*").replace("÷", "/").replace("%", "/100")
        try:
            val = eval(s)
        except:
            return "Error"

        return self.fmt_num(val)


class CalculatorMachine:
    def __init__(self, update_result):
        self.calc = Calculator()
        self.formula = ""
        self.state = 0
        self.result_prefix = "="
        self.result = ""
        self.update_result = update_result
        update_result("", "=")

    def input(self, c):
        if c not in "0123456789+-*/%()=!A":
            return
        if c == "A":
            self.formula = ""
            self.result = "0"
            self.update_result(self.formula, self.result_prefix + self.result)
            return
        if self.state == 0:
            if c == "=" or c == "!":
                return
            if (
                self.result != ""
                and self.result != "Error"
                and (c == "+" or c == "-" or c == "*" or c == "/" or c == "%")
            ):
                self.formula = self.result + c
                self.result = ""
                self.update_result(self.formula, self.result_prefix + self.result)
                self.state = 1
                return
            self.formula = c
            self.update_result(self.formula, "")
            self.state = 1
            return
        if self.state == 1:
            if c == "=":
                self.result = self.calc(self.formula)
                self.update_result(self.formula, self.result_prefix + self.result)
                self.formula = self.result
                self.state = 0
                return
            if c == "!":
                self.formula = self.formula[:-1]
                self.update_result(self.formula, "")
                return
            self.formula += c
            self.update_result(self.formula, "")
            return
