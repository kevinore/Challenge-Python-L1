import os
from app import app, db
from app.models import Time
from flask import render_template
from app.routes.functions import getRegions, getCountries, createDataFrrame

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/region', methods=["GET"])
def region_table():

    regions = getRegions()
    countries = getCountries(regions)
    df = createDataFrrame(countries)

    total = df['Time (seconds)'].sum()
    minimum = df['Time (seconds)'].min()
    max = df['Time (seconds)'].max()
    avg = df['Time (seconds)'].mean()


    times = Time(total=total, minimum=minimum, max=max, average=avg)
    db.session.add(times)
    db.session.commit()

    return render_template('region.html',
                column_names=df.columns.values,
                row_data=list(df.values.tolist()),
                link_column="Patient ID",
                zip=zip,
                total = total,
                minimum = minimum,
                max = max,
                avg = avg)
