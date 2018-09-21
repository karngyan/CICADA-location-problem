import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import make_response

app = dash.Dash()
server = app.server
app.title = 'Cicada Location | Eat the ****** to get the flag'
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})
app.config['suppress_callback_exceptions']=True


app.layout = html.Div([

    html.Div(dcc.Input(id='input-box', 
                    type='text',
                    value='',
                    placeholder='Nom! Nom! Nom!',
                    style = {'width': '100%'}         
            )
        ),

    html.Div(
        children = [
            html.Button('Submit', 
                id='button',
            ),
            html.Div(id='output-container-button',
                children='Enter a value and press submit'
            )
        ],
    )

], style = {'position':'absolute', 'top': '50%', 'left': '50%' ,'transform' : 'translate(-50%,-50%)'})

@server.route('/flag')
def setcookie():
    resp = make_response('Congrats! you finally got it.')
    resp.set_cookie('flag', 'time_to_run_to_Laxmi')
    return resp

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    if(value == 'flag'):
        setcookie()
        return 'Congrats! You got it, right? No? ;)\nMove to ./flag'
    else:
        return 'Enter a value and press submit'
        



if __name__ == '__main__':
    app.run_server(debug=True)