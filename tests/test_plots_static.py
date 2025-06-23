import random
import chartify
import numpy as np
import pandas as pd

"""Convenience test-ready plots for manual analysis."""

def main():
    data = chartify.examples.example_data()
    print(data.head())

    # *** Set c to any test method here ***
    c = test_area_disallow_nan(data)

    c.show()

def test_horizontal_stacked_bar(df):
    c = chartify.Chart(blank_labels=True, y_axis_type="categorical")
    data = df.groupby(["fruit", "country"])["quantity"].sum().reset_index()
    c.set_title('Stacked Horizontal Bar chart')
    c.set_subtitle('Stacked columns by a categorical factor.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.bar_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        normalize=False,
    )

    return c

def test_horizontal_stacked_bar_text_total(df):
    c = chartify.Chart(blank_labels=True, y_axis_type="categorical")
    data = df.groupby(["fruit", "country"])["quantity"].sum().reset_index()
    c.set_title('Stacked Horizontal Bar chart')
    c.set_subtitle('Stacked columns by a categorical factor.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.bar_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        normalize=False,
    )

    c.plot.text_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        text_column="quantity",
        text_color="white",
    )

    c.style.color_palette.reset_palette_order()
    c.plot.text_stacked_total(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        text_color="black"
    )

    return c

def test_vertical_stacked_bar(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="categorical")
    data = df.groupby(["fruit", "country"])["quantity"].sum().reset_index()
    c.set_title('Stacked Vertical Bar chart')
    c.set_subtitle('Stacked columns by a categorical factor.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.bar_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        normalize=False,
    )

    return c

def test_vertical_stacked_bar_text_total(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="categorical")
    data = df.groupby(["fruit", "country"])["quantity"].sum().reset_index()
    c.set_title('Stacked Vertical Bar chart')
    c.set_subtitle('Stacked columns by a categorical factor.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.bar_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        normalize=False,
    )

    c.plot.text_stacked(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        text_column="quantity",
        text_color="white",
    )

    c.style.color_palette.reset_palette_order()
    c.plot.text_stacked_total(
        data_frame=data,
        categorical_columns=["fruit"],
        numeric_column="quantity",
        stack_column="country",
        text_color="black"
    )

    return c

def test_pie(df):
    c = chartify.Chart(x_axis_type="categorical", y_axis_type="categorical")
    data = df.groupby("fruit")["quantity"].sum().reset_index()
    c.set_title('Pie chart')
    c.set_subtitle('A pie chart showing the quantity of each fruit.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.pie(
        data_frame=data,
        categorical_column="fruit",
        numeric_column="quantity",
        color_column="fruit",
    )

    return c

def test_area_allow_nan(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    c.set_title('Unstacked Area chart - Allow NAN')
    c.set_subtitle('Show overlapping values. Automatically adjusts opacity.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')

    data = df
    data = data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "country",],).sum().reset_index().sort_values("date")
    data = data[data.country != 'GB']
    data = data[data.country != 'BR']

    # Delete at ends for US and CA
    data['unit_price'].iloc[-1] = np.nan
    data['total_price'].iloc[-1] = np.nan
    data['unit_price'].iloc[-2] = np.nan
    data['total_price'].iloc[-2] = np.nan
    data['unit_price'].iloc[-4] = np.nan
    data['total_price'].iloc[-4] = np.nan

    # Delete 2 US in middle of area
    data['unit_price'].iloc[-18] = np.nan
    data['total_price'].iloc[-18] = np.nan
    data['unit_price'].iloc[-19] = np.nan
    data['total_price'].iloc[-19] = np.nan

    c.plot.area(
        data_frame=data,
        x_column='date',
        y_column='total_price',
        second_y_column='unit_price',
        color_column='country',
        stacked=False,
        allow_nan=True,
    )

    return c

def test_area_disallow_nan(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    c.set_title('Unstacked Area chart - Disallow NAN')
    c.set_subtitle('Show overlapping values. Automatically adjusts opacity.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')

    data = df
    data = data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "country",],).sum().reset_index().sort_values("date")
    data = data[data.country != 'GB']
    data = data[data.country != 'BR']

    # Delete at ends for US and CA
    data['unit_price'].iloc[-1] = np.nan
    data['total_price'].iloc[-1] = np.nan
    data['unit_price'].iloc[-2] = np.nan
    data['total_price'].iloc[-2] = np.nan
    data['unit_price'].iloc[-4] = np.nan
    data['total_price'].iloc[-4] = np.nan

    # Delete 2 US in middle of area
    data['unit_price'].iloc[-18] = np.nan
    data['total_price'].iloc[-18] = np.nan
    data['unit_price'].iloc[-19] = np.nan
    data['total_price'].iloc[-19] = np.nan

    c.plot.area(
        data_frame=data,
        x_column='date',
        y_column='total_price',
        second_y_column='unit_price',
        color_column='country',
        stacked=False,
        allow_nan=False,
    )

    return c

def test_parallel(df):
    data = df
    total_quantity_by_month_and_fruit = (
        data.groupby([data["date"] + pd.offsets.MonthBegin(-1), "fruit"])["quantity"]
        .sum()
        .reset_index()
        .rename(columns={"date": "month"})
        .sort_values("month")
    )
    
    total_quantity_by_month_and_fruit = total_quantity_by_month_and_fruit[total_quantity_by_month_and_fruit.fruit != 'Apple']
    total_quantity_by_month_and_fruit = total_quantity_by_month_and_fruit[total_quantity_by_month_and_fruit.fruit != 'Grape']
    total_quantity_by_month_and_fruit['total_price'] = df['total_price']

    total_quantity_by_month_and_fruit['quantity'].iloc[8:10] = np.nan
    total_quantity_by_month_and_fruit['quantity'].iloc[-7:] = np.nan
    total_quantity_by_month_and_fruit['quantity'].iloc[-1] = -10

    print(total_quantity_by_month_and_fruit)

    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    c.set_title('Unstacked Area chart')
    c.set_subtitle('Show overlapping values. Automatically adjusts opacity.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Number of fruits')
    c.style.set_color_palette('categorical', 'Dark2')
    c.plot.area(
        data_frame=total_quantity_by_month_and_fruit,
        x_column='month',
        y_column='quantity',
        second_y_column='total_price',
        color_column='fruit',
        stacked=False,
        allow_nan=True,
    )
    
    return c

def test_horizontal_categorical_cumulative_histogram(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="density")
    c.set_title('Cumulative Histogram')
    c.set_subtitle('A cumulative histogram showing the distribution of fruit prices.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Cumulative count')
    c.plot.cumulative_histogram(
        data_frame=df,
        values_column="unit_price",
        color_column="fruit",
    )

    return c

def test_horizontal_unified_cumulative_histogram(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="density")
    c.set_title('Cumulative Histogram')
    c.set_subtitle('A cumulative histogram showing the distribution of fruit prices.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Unit price for a fruit batch')
    c.axes.set_yaxis_label('Cumulative count')
    c.plot.cumulative_histogram(
        data_frame=df,
        values_column="unit_price",
    )

    return c

def test_vertical_categorical_cumulative_histogram(df):
    c = chartify.Chart(blank_labels=True, y_axis_type="density")
    c.set_title('Cumulative Histogram')
    c.set_subtitle('A cumulative histogram showing the distribution of fruit prices.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Cumulative count')
    c.axes.set_yaxis_label('Unit price for a fruit batch')
    c.plot.cumulative_histogram(
        data_frame=df,
        values_column="unit_price",
        color_column="fruit",
    )

    return c

def test_vertical_unified_cumulative_histogram(df):
    c = chartify.Chart(blank_labels=True, y_axis_type="density")
    c.set_title('Cumulative Histogram')
    c.set_subtitle('A cumulative histogram showing the distribution of fruit prices.')
    c.set_source_label('Source: Example Data')
    c.axes.set_xaxis_label('Cumulative count')
    c.axes.set_yaxis_label('Unit price for a fruit batch')
    c.plot.cumulative_histogram(
        data_frame=df,
        values_column="unit_price",
    )

    return c

def test_line_hoverable(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    price_by_date = df.groupby("date")["total_price"].sum().reset_index()  # Move 'date' from index to column

    # Plot the data
    c.set_title("Line charts")
    c.set_subtitle("Plot two numeric values connected by an ordered line.")

    # price_by_date["date"] = price_by_date["date"].apply(lambda x : str(x.date()))
    c.plot.line(   
        data_frame=price_by_date.sort_values("date"),
        x_column="date",
        y_column="total_price",
        hoverable=True,
        hover_info=[("date", "@date{%F}"), ("total_price", "@total_price")],
        hover_formatters={"@date": "datetime"},
        hover_mode="vline",
    )

    return c

def test_scatter_hoverable(df):
    c = chartify.Chart(blank_labels=True, x_axis_type="datetime")
    c.plot.scatter(data_frame=df, x_column="date", y_column="unit_price", hoverable=True, hover_formatters={})
    c.set_title("Scatterplot")
    c.set_subtitle("Plot two numeric values.")
    
    return c

if __name__ == '__main__':
    main()
