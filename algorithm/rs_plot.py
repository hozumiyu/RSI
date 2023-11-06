import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px
['Li', 'Be', 'B', 'C', 
 'N', 'O', 'Ne', 'P', 
 'S', 'C', 'Br', 'Cl', 'Ra', 'Fr']
color  = px.colors.qualitative.Light24
color[1] = color[10]
color[6] = color[9]
    
color_discrete_map= { str(idx): color[idx-1] for idx in range(1, 15)}   #map label to new color
#color = px.colors.qualitative.Light24   #color map
#color_discrete_map= { str(idx): color[idx-1] for idx in range(1, 25)}   #map label to new color
symbol_discrete_map = {'1': 'circle-open', '2': 'diamond-open', '3': 'square-open', '4': 'cross-open', 
                       '5': 'x-open', '6': 'triangle-up-open', '7': 'triangle-down-open', '8': 'triangle-left-open',
                       '9': 'triangle-right-open', '10': 'triangle-ne-open', '11': 'triangle-se-open', 
                       '12': 'triangle-sw-open', '13': 'triangle-nw-open', '14': 'pentagon-open',
                       '15': 'star-open', '16':'hexagram-open', '17': 'star-square-open',
                       '18': 'star-diamond-open', '19': 'diamond-tall-open', '20': 'diamond-wide-open'}    #map label to symbols
#color_discrete_map['7'] = color[9]
#color_discrete_map['4'] = color[10]
def adjustCoordinate(rs_score, y, max_col = None):
    rs_score_new = rs_score.copy()
    label_ls = list(set(list(y)))
    total_labels = len(label_ls)
    if max_col == None:
        max_col = int( np.ceil(np.sqrt(total_labels)))
    max_row = int( np.ceil(total_labels/  max_col))
    
    current_col = 0
    current_row = max_row - 1
    
    for label in label_ls:
        index = np.where(y == label)[0]
        rs_score_new[index, 0] +=  current_col
        rs_score_new[index, 1] += current_row
        
        current_col += 1
        if current_col == max_col:
            current_col = 0 
            current_row -= 1
    return rs_score_new


def constructFigure(rs_score, y, color_discrete_map = color_discrete_map, 
                    symbol_discrete_map = symbol_discrete_map):
    '''
        Input:
            rs_score: residue-similarity score. If you are plotting all the classes, make sure you run adjustCoordinate first
            y: the color you want to use to color the rs-plot. (I used y_pred to color the points)
    '''
    df = {'x': rs_score[:, 0], 'y': rs_score[:, 1], 'label':y.astype(int)+1}   #creat dictionary of points
    df['label'] = df['label'].astype('str')   #convert preicted labels to stirng -> allows discrete colors
    
    fig = px.scatter(df, x = 'x', y = 'y', color = 'label', symbol = 'label', 
                 color_discrete_map=color_discrete_map, symbol_map=symbol_discrete_map)  #Construct figure with discrete color and custom symbols
    fig.update_traces(marker=dict(size=20,
                              line=dict(width=3,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))   #size and line width of markers
    
    max_x = int(np.ceil(np.max(rs_score[:, 0]))); min_x =  int(np.floor(np.min(rs_score[:, 0])))
    max_y = int(np.ceil(np.max(rs_score[:, 1]))); min_y =  int(np.floor(np.min(rs_score[:, 1])))
    #fig.add_vline(x=min_x - 0.01, line_width=3, line_color = 'black')  #add the borders
    #fig.add_vline(x=max_x + 0.01, line_width=3, line_color = 'black')   #add the borders
    #fig.add_hline(y=max_y + 0.01, line_width=3, line_color = 'black')  #add the borders
    #fig.add_hline(y=min_y - 0.01, line_width=3, line_color = 'black')#addE the borders
    for idx in np.arange(min_x, max_x+1):
        fig.add_vline(x = idx+0.05, line_width=2, line_color = 'black')
    
    for idx in np.arange(min_y, max_y+1):
        fig.add_hline(y = idx + 0.05, line_width=2, line_color = 'black')
    
    fig.update_xaxes(range=[min_x+ 0.05 , max_x + 0.05])  #fix the range of x
    
    
    fig.update_yaxes(range=[min_y+ 0.05, max_y + 0.05])  #fix the range of y
    
    
    fig.update_layout({ax:{"visible":False, "matches":None} for ax in fig.to_dict()["layout"] if "axis" in ax}) #remove ticks
    
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')  #make background white
    
    #Remove all the legends. Comment this out if you want the legends
    for trace in fig['data']: 
        trace['showlegend'] = False
        
    fig.update_layout(legend={'title_text':''})  #remove title
    
    
    return fig

