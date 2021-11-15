
class CustomerList():

    @staticmethod
    def get_customer_list(meta_dict, customer_dict):

        return {
            "meta": meta_dict,
            "objects": customer_dict
        }