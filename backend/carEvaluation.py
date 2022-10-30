from model import input_lvs, output_lv, rule_base
import inference_mamdani


def carEvaluation(age, mileage, repairments):
    inference_mamdani.preprocessing(input_lvs, output_lv)
    crisp_values = (age, mileage, repairments)
    result = inference_mamdani.process(input_lvs, output_lv, rule_base, crisp_values)
    print(crisp_values, result)
    return result


# carEvaluation(3, 4, 5)
# for lv in model.input_lvs:
#     fuzzy_operators.draw_lv(lv)
# fuzzy_operators.draw_lv(model.output_lv)
