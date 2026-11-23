class LoyaltyPoint:
    POINTS_2_PAISA = 1/10
 
    @staticmethod
    def calculate(payment):
        return int(payment.amount/100 )

    @staticmethod
    def calculate_paisa(points):
        return int(points*LoyaltyPoint.POINTS_2_PAISA)


    