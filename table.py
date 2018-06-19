#!/usr/bin/python

import plotly


def basic_table(services):

    # DESCRIBE TABLE
    trace = plotly.graph_objs.Table(
        # DESCRIBE TABLE HEADERS
        header=dict(
            values=[
                'Name',
                'Version',
                'Desired Count',
                'Running Count',
                'Cluster',
                'Launch Type'
            ],
            fill=dict(color='#a1c3d1')
        ),
        # DESCRIBE TABLE CONTENTS
        cells=dict(
            values=[
                [service['name'] for service in services],
                [service['version'] for service in services],
                [service['desired_count'] for service in services],
                [service['running_count'] for service in services],
                [service['cluster'] for service in services],
                [service['launch_type'] for service in services]
            ],
            fill=dict(
                color=['#F5F4F4',
                       '#F5F4F4',
                       ['#24F015' if service['desired_count'] == service['running_count'] else '#DA100C' for service in services],
                       ['#24F015' if service['desired_count'] == service['running_count'] else '#DA100C' for service in services],
                       '#F5F4F4',
                       '#F5F4F4']
            )
        )
    )

    data = [trace]
    plotly.offline.plot(data, filename='basic_table.html')
    return
