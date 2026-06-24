from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)
app.title = "Soul Foods - Pink Morsel Visualizer"

# Load the processed sales dataset
df = pd.read_csv('formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Layout of the dashboard matching the custom stylesheet
app.layout = html.Div(className='dashboard-container', children=[
    # Header Section
    html.Div(className='dashboard-header', children=[
        html.H1("Soul Foods: Pink Morsel Visualizer", className='dashboard-title'),
        html.H3("Analyzing sales performance before and after the January 15, 2021 price change.", className='dashboard-subtitle')
    ]),
    
    # Controls Section (Radio buttons for region selection)
    html.Div(className='control-card', children=[
        html.Div("Filter by Region", className='control-label'),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            className='radio-group',
            inputStyle={"margin-right": "8px", "accent-color": "#3b82f6"}
        )
    ]),
    
    # Visualization Section
    html.Div(className='chart-card', children=[
        dcc.Graph(
            id='sales-line-chart',
            config={'displayModeBar': False} # Keep the UI clean by hiding the mode bar
        )
    ])
])

# Callback to dynamically update the line chart based on the selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    # Filter the dataset by selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
        
    # Group by date to aggregate sales
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    
    # Construct the Plotly Express line chart
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        color_discrete_sequence=['#3b82f6'], # Premium vibrant blue line
        labels={'date': 'Date', 'sales': 'Sales ($)'}
    )
    
    # Add vertical line for the January 15, 2021 price increase event
    # Using millisecond timestamp since the x-axis uses datetime objects
    event_date = pd.to_datetime('2021-01-15')
    fig.add_vline(
        x=event_date.timestamp() * 1000,
        line_width=2,
        line_dash='dash',
        line_color='#ef4444', # Sleek modern red
        annotation_text='Price Increase (Jan 15, 2021)',
        annotation_position='top left',
        annotation_font_color='#f8fafc',
        annotation_font_size=11
    )
    
    # Sleek Dark/Slate Theme styling matching the CSS wrapper
    fig.update_layout(
        paper_bgcolor='rgba(0, 0, 0, 0)', # Transparent background
        plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot canvas
        font_color='#94a3b8',              # Slate light text
        title={
            'text': f"Sales Trends - {selected_region.capitalize()} Region",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 16, 'color': '#cbd5e1', 'family': 'Inter'}
        },
        xaxis={
            'title': 'Date',
            'showgrid': True,
            'gridcolor': 'rgba(255, 255, 255, 0.05)',
            'linecolor': 'rgba(255, 255, 255, 0.1)',
            'zeroline': False
        },
        yaxis={
            'title': 'Sales Revenue ($)',
            'showgrid': True,
            'gridcolor': 'rgba(255, 255, 255, 0.05)',
            'linecolor': 'rgba(255, 255, 255, 0.1)',
            'zeroline': False
        },
        hovermode='x unified',
        margin={'t': 60, 'b': 40, 'r': 20, 'l': 20}
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
