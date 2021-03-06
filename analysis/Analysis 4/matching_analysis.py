import pandas as pd

def matching_color_aggregation(matching_output):
    input_links = matching_output['input_image']
    input_links = list(dict.fromkeys(input_links))
    # all_input_colors = set()
    # color_matching_score = dict()

    result = []
    for j in range(1,4):
        count_top1 = 0
        count_top2 = 0
        count_top3 = 0
        count = 0
        df = matching_output[['matching_col1', 'matching_col2', 'matching_col3', 'top'+ str(j)+'_color']]
        for index, hit in df.iterrows():
            count += 1
            if hit['top' + str(j) + '_color'] == hit['matching_col1']:
                count_top1 += 1
            if hit['top' + str(j) + '_color'] == hit['matching_col2']:
                count_top2 += 1
            if hit['top' + str(j) + '_color'] == hit['matching_col3']:
                count_top3 += 1
        result.append(('rank' + str(j)+ ' matching', cal_percent(count_top1, count), cal_percent(count_top2, count), cal_percent(count_top3, count)))
    return result 

def cal_percent(number, count):

    return float(number) / float(count) * 100 

def matching_style_aggregation(matching_output):
    input_links = matching_output['input_image']
    input_links = list(dict.fromkeys(input_links))

    result = []
    for j in range(1,4):
        count_top1 = 0
        count_top2 = 0
        count_top3 = 0
        count = 0
        df = matching_output[['matching_style1', 'matching_style2', 'matching_style3', 'top'+ str(j)+'_style']]
        for index, hit in df.iterrows():
            count += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style1']:
                count_top1 += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style2']:
                count_top2 += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style3']:
                count_top3 += 1
        result.append((cal_percent(count_top1, count), cal_percent(count_top2, count), cal_percent(count_top3, count)))

    return result 

def matching_style_color_aggregation(matching_output):
    input_links = matching_output['input_image']
    input_links = list(dict.fromkeys(input_links))

    result = []
    for j in range(1,4):
        count_top1 = 0
        count_top2 = 0
        count_top3 = 0
        count = 0
        df = matching_output[['matching_style1', 'matching_style2', 'matching_style3', 'top'+ str(j)+'_style', 'matching_col1', 'matching_col2', 'matching_col3', 'top'+ str(j)+'_color']]
        for index, hit in df.iterrows():
            count += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style1'] and hit['top' + str(j) + '_color'] == hit['matching_col1'] :
                count_top1 += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style2'] and hit['top' + str(j) + '_color'] == hit['matching_col2'] :
                count_top2 += 1
            if hit['top' + str(j) + '_style'] == hit['matching_style3'] and hit['top' + str(j) + '_color'] == hit['matching_col3'] :
                count_top3 += 1
        result.append((cal_percent(count_top1, count), cal_percent(count_top2, count), cal_percent(count_top3, count)))

    return result 
def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('hit3_top_three_result.csv')

    result_color = matching_color_aggregation(mturk_res)
    result_style = matching_style_aggregation(mturk_res)
    result_style_color = matching_style_color_aggregation(mturk_res)
    
    df1 = pd.DataFrame(result_color, columns = ['Matching rank', 'top1_color', 'top2_color', 'top3_color'])
    df2 = pd.DataFrame(result_style, columns = ['top1_style', 'top2_style', 'top3_style'])
    df3 = pd.DataFrame(result_style_color, columns = ['top1_style_color', 'top2_style_color', 'top3_style_color'])
    df = pd.concat([df1, df2, df3], axis=1)
    df.to_csv('matching_analysis.csv', index=False)

if __name__ == '__main__':
    main()

