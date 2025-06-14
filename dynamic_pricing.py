class DynamicPricing:
    HIGH_SEASON = [(6, 7, 8)]  # June, July, August (as tuples for simplicity)

    @staticmethod
    def apply_seasonal_price(base_price, check_in_month):
        if check_in_month in DynamicPricing.HIGH_SEASON[0]:
            return base_price * 1.3  # 30% higher in high season
        else:
            return base_price * 0.9  # 10% lower in low season
