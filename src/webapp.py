import dash
# https://dash.plot.ly/dash-core-components
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import src.dbUtils as utils
from datetime import datetime as dt
from mongoengine.queryset.visitor import Q

db = utils.connectDB()
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
# df = utils.bookingQueryAsDf()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='Dash: A web application framework for Python.'),

    html.H2("filter results"),

    html.Label("pick the month"),
    dcc.DatePickerRange(
            id='date-picker',
            min_date_allowed=dt(2015, 1, 1),
            initial_visible_month=dt(2019, 12, 5),
            display_format="D-M-YYYY",
            clearable=True
    ),
    html.Button("Filter", id="filter-button"),

    dash_table.DataTable(
            id='table-abc',
            columns=[],
            data=[],
            style_cell={'textAlign': 'left',
                        "padding"  : '1em'},
            style_header={'fontWeight': 'bold',
                          'textAlign' : 'left'},
            style_cell_conditional=[{
                'if'       : {'column_id': 'price'},
                'textAlign': 'right'
            }]
    )
])


@app.callback(
        [Output(component_id="table-abc", component_property="data"),
         Output("table-abc", "columns")],
        [Input("filter-button", "n_clicks")],
        [State("date-picker", "start_date"),
         State("date-picker", "end_date")]
)
def update_table(n_clicks, start_date, end_date):
    query_args = []
    if (start_date is None) and (end_date is None):
        pass
    else:
        if start_date is None:
            start_date = end_date - dt.month
        if end_date is None:
            end_date = start_date + dt.month
        query_args.append(Q(dates__checkIn__lt=end_date) &
                          Q(dates__checkOut__gt=start_date))
    df = utils.bookingQueryAsDf(*query_args)
    return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns]


if __name__ == '__main__':
    # with debug=True, we got "hot-reloading"!
    app.run_server(debug=True)
