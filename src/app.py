import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import sqlite3


app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(
    [
        dcc.Input(placeholder='Write name here', id='input-val'),
        html.Button('submit', id='button-id', n_clicks=0),
        html.Div(id='output-val')
    ]
)


@app.callback(
    Output('output-val', 'children'),
    Input('button-id', 'n_clicks'),
    State('input-val', 'value')
)
def callbk(n_clicks, input_val):
    if n_clicks > 0 and input_val:
        conn = sqlite3.connect('db_name.db')
        cursor = conn.cursor()
          
        insert_query = "INSERT INTO test_table (name, name2) VALUES (?, ?)"
        cursor.execute(insert_query, (input_val, 'extra_col'))
        conn.commit()
        cursor.close()
        conn.close()

        return f'{input_val} value has been entered'
    return ''


if __name__ == '__main__':
    app.run_server(debug=True)
