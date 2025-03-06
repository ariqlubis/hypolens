class Result:
    def __init__(self, method: str, statistic: float, p_value: float, alpha: float, significant: bool):
        self.method = method
        self.statistic = statistic
        self.p_value = p_value
        self.alpha = alpha
        self.significant = significant

    def __repr__(self):
        return (
            f"Result(method={self.method}, statistic={self.statistic}, "
            f"p_value={self.p_value}, alpha={self.alpha}, significant={self.significant})"
        )
