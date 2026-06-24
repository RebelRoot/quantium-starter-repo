from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = Dash(__name__)

# Load the formatted sales data
df = pd.read_csv('formatted_data.csv')

# Ensure date is in datetime format and sort by date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Group by date to get daily sales across all regions
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Create the line chart
fig = px.line(
    daily_sales, 
    x='date', 
    y='sales', 
    title='Pink Morsel Sales Trend Analysis',
    labels={'date': 'Date', 'sales': 'Sales Revenue ($)'}
)

# Add a vertical line to mark the price increase event on January 15, 2021
fig.add_vline(
    x=pd.to_datetime('2021-01-15').timestamp() * 1000, # Plotly requires timestamps in milliseconds for vlines on datetime axes
    line_width=2, 
    line_dash='dash', 
    line_color='red',
    annotation_text='Price Increase (Jan 15, 2021)', 
    annotation_position='top left'
)

# Customize the chart layout for maximum clarity
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Total Sales Revenue ($)',
    title_x=0.5,
    template='plotly_white',
    hovermode='x unified'
)

# Define layout structure
app.layout = html.Div(style={'fontFamily': 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 'padding': '40px', 'backgroundColor': '#f8f9fa', 'minHeight': '100vh'}, children=[
    html.Div(style={'maxWidth': '1200px', 'margin': '0 auto', 'backgroundColor': '#ffffff', 'padding': '30px', 'borderRadius': '8px', 'boxShadow': '0 4px 6px rgba(0,0,0,0.1)'}, children=[
        html.H1(
            children='Soul Foods: Pink Morsel Visualizer',
            style={'textAlign': 'center', 'color': '#2c3e50', 'fontWeight': '600', 'margin': '0 0 10px 0'}
        ),
        
        html.H3(
            children='Analyzing sales impact before and after the January 15, 2021 price increase.',
            style={'textAlign': 'center', 'color': '#7f8c8d', 'fontWeight': '400', 'margin': '0 0 30px 0'}
        ),
        
        dcc.Graph(
            id='sales-chart',
            figure=fig
        )
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
