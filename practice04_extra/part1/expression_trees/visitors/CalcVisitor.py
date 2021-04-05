class CalcVisitor:
    def visit(self, expression):
        return expression.count()
