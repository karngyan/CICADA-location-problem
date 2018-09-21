import dash,string,random
import dash_core_components as dcc
import dash_html_components as html
from flask import make_response,Response

app = dash.Dash()
server = app.server
app.title = 'Cicada Location | v2'
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.config['suppress_callback_exceptions']=True


app.layout = html.Div([

    html.Div(dcc.Input(id='input-box', 
                    type='text',
                    value='',
                    placeholder='What are you looking for?',
                    style = {'width': '100%'}         
            )
        ),

    html.Div(
        children = [
            html.Button('Submit', 
                id='button',
            ),
            html.Div(id='output-container-button',
                children='Enter a value and press submit!'
            )
        ],
    )

], style = {'position':'absolute', 'top': '50%', 'left': '50%' ,'transform' : 'translate(-50%,-50%)'})

@server.route('/Laxmi_Canteen_has_the_best_Dal_in_BIT')
def setcookie():
    resp = make_response('Alright! You have come this far. Kudos to you. To get the final flag you need to cook it up.')
    resp.set_cookie('flag', 'C0okies_are_not_biscuits')
    return resp


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    if(n_clicks > 0):
        if(value == 'flag'):
            return 'Congrats! This was an easy one, here is the flag: Laxmi_Canteen_has_the_best_Dal_in_BIT'
        else:
            return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
        



if __name__ == '__main__':
    app.run_server(debug=True)


