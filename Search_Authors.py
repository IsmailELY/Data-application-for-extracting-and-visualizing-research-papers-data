import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

auth_data = [{'date_registered': '2019-05-17T14:48:28.860798', 'locale': 'en_US', 'full_name': 'Ali Hussein', 'id': 'fpgxw', 'artpub': 1}, {'date_registered': '2019-03-16T08:27:58.019770', 'locale': 'en_US', 'full_name': 'Ifeoma Emmanuela Udoye', 'id': 'pdz85', 'artpub': 3}, {'date_registered': '2019-05-01T14:36:02.179882', 'locale': 'en_US', 'full_name': 'Shalote Chipamaunga', 'id': 'b29e6', 'artpub': 1}, {'date_registered': '2019-05-01T15:10:19.593904', 'locale': 'en_US', 'full_name': 'Detlef Prozesky', 'id': 'nqvh9', 'artpub': 1}, {'date_registered': '2019-04-11T20:34:00.555147', 'locale': 'en_US', 'full_name': 'Anthony Ikechukwu Ezeogamba', 'id': 'hgxja', 'artpub': 2}, {'date_registered': '2018-12-03T22:08:33.198846', 'locale': 'en_US', 'full_name': 'Tom  L. Osborn', 'id': 'wne4y', 'artpub': 1}, {'date_registered': '2019-04-12T13:39:17.222571', 'locale': 'en_US', 'full_name': 'Neil Hart', 'id': '9k8u4', 'artpub': 1}, {'date_registered': '2019-04-17T15:27:58.598963', 'locale': 'en_US', 'full_name': 'Richard Washington', 'id': 'uysw4', 'artpub': 1}, {'date_registered': '2019-04-17T15:28:38.472843', 'locale': 'en_US', 'full_name': 'Ross Maidment', 'id': 'fv4e5', 'artpub': 1}, {'date_registered': '2019-04-06T20:01:49.506895', 'locale': 'en_US', 'full_name': 'ifeoma udoye', 'id': 'ebnys', 'artpub': 1}, {'date_registered': '2017-12-15T18:42:27.178887', 'locale': 'fr', 'full_name': 'Bado', 'id': 'jusma', 'artpub': 2}, {'date_registered': '2016-04-19T21:21:55.336000', 'locale': 'en_US', 'full_name': 'Timo B. Roettger', 'id': 'nmqfr', 'artpub': 1}, {'date_registered': '2019-01-31T16:17:55.383113', 'locale': 'en_US', 'full_name': 'Dr. Samuel Ssekajja', 'id': 'gqxbp', 'artpub': 8}, {'date_registered': '2019-01-24T16:07:10.403746', 'locale': 'en_US', 'full_name': 'Bassey Godwin', 'id': 'jtfwp', 'artpub': 1}, {'date_registered': '2017-08-02T14:00:10.188646', 'locale': 'en_US', 'full_name': 'Kersten Bergstrom', 'id': '9r8yk', 'artpub': 1}, {'date_registered': '2019-01-04T17:58:55.307410', 'locale': 'en_US', 'full_name': 'Austin B. Lawrence', 'id': 'jfpqe', 'artpub': 1}, {'date_registered': '2019-01-04T17:59:35.886478', 'locale': 'en_US', 'full_name': 'Alex J. Pelissero', 'id': 'zj47n', 'artpub': 1}, {'date_registered': '2019-01-04T18:00:00.355138', 'locale': 'en_US', 'full_name': 'Lauren J. Hammond', 'id': 'fty87', 'artpub': 1}, {'date_registered': '2019-01-04T18:01:30.837995', 'locale': 'en_US', 'full_name': 'Eliwasa Maro', 'id': 'czb32', 'artpub': 1}, {'date_registered': '2019-01-04T18:01:59.637381', 'locale': 'en_US', 'full_name': 'Henry T. Bunn', 'id': '9h6wp', 'artpub': 1}, {'date_registered': '2019-01-04T18:02:36.867718', 'locale': 'en_US', 'full_name': 'Charles M. Musiba', 'id': 'mdtja', 'artpub': 1}, {'date_registered': '2018-12-07T12:58:25.833322', 'locale': 'en_US', 'full_name': 'Philip Rodenbough', 'id': 'n8fkb', 'artpub': 1}, {'date_registered': '2018-12-07T13:05:26.246811', 'locale': 'en_US', 'full_name': 'Majuto Clement Manyilizu', 'id': 'h5yj9', 'artpub': 1}, {'date_registered': '2018-05-10T18:24:16.065245', 'locale': 'en_US', 'full_name': 'Justin Sègbédji Ahinon', 'id': 'pfx7j', 'artpub': 2}, {'date_registered': '2018-06-21T22:56:28.582594', 'locale': 'en_US', 'full_name': 'Johanna Havemann', 'id': 'bjvtq', 'artpub': 1}, {'date_registered': '2018-05-11T21:42:07.071173', 'locale': 'en_US', 'full_name': 'Taa Nguimbis Esseme  Benedict', 'id': '2g3zt', 'artpub': 1}, {'date_registered': '2018-11-01T12:40:43.851953', 'locale': 'en_US', 'full_name': 'Mbondji Ebongué', 'id': 'a9652', 'artpub': 1}, {'date_registered': '2018-10-04T17:19:57.410071', 'locale': 'en_US', 'full_name': 'Cesilia Mambile', 'id': 'z6c5v', 'artpub': 2}, {'date_registered': '2018-10-04T18:06:06.937027', 'locale': 'en_US', 'full_name': 'Dina Machuve', 'id': 'nv84w', 'artpub': 2}, {'date_registered': '2018-10-04T18:45:44.304124', 'locale': 'en_US', 'full_name': 'Sabine Moebs', 'id': 'ynkxt', 'artpub': 1}, {'date_registered': '2018-09-08T23:05:02.651769', 'locale': 'en_US', 'full_name': 'Redouane  SAHBATOU', 'id': 'mtsvu', 'artpub': 2}, {'date_registered': '2018-07-12T08:46:01.246373', 'locale': 'en_US', 'full_name': 'Ademola Adeifeoba', 'id': 'btf5y', 'artpub': 2}, {'date_registered': '2018-09-10T10:29:10.777332', 'locale': 'en_US', 'full_name': 'Obasegun Tekena Ayodele', 'id': '5np4c', 'artpub': 2}, {'date_registered': '2018-07-23T07:16:27.290147', 'locale': 'en_US', 'full_name': 'Rebecca Rogers Ackermann', 'id': 'j7xtn', 'artpub': 4}, {'date_registered': '2018-08-28T13:00:49.085947', 'locale': 'en_US', 'full_name': 'Michael Arnold', 'id': '6kmr3', 'artpub': 1}, {'date_registered': '2018-08-28T13:13:54.609542', 'locale': 'en_US', 'full_name': 'Marcella Baiz', 'id': 'zwbng', 'artpub': 1}, {'date_registered': '2018-08-28T13:02:07.072365', 'locale': 'en_US', 'full_name': 'James A Cahill', 'id': 'tjx47', 'artpub': 1}, {'date_registered': '2018-08-28T13:03:56.573082', 'locale': 'en_US', 'full_name': 'Liliana Cortés-Ortiz', 'id': 't78xe', 'artpub': 1}, {'date_registered': '2018-08-28T13:07:00.877099', 'locale': 'en_US', 'full_name': 'Ben J Evans', 'id': '9xghu', 'artpub': 1}, {'date_registered': '2018-08-28T13:08:50.041063', 'locale': 'en_US', 'full_name': 'B Rosemary Grant', 'id': 'kxamd', 'artpub': 1}, {'date_registered': '2018-08-28T13:07:58.304657', 'locale': 'en_US', 'full_name': 'Peter R Grant', 'id': 'ae4w3', 'artpub': 1}, {'date_registered': '2018-08-28T13:09:38.126314', 'locale': 'en_US', 'full_name': 'Benedikt Hallgrimsson', 'id': 'nfe3g', 'artpub': 1}, {'date_registered': '2018-08-28T13:10:18.355453', 'locale': 'en_US', 'full_name': 'Robyn Humphreys', 'id': 'wmcrd', 'artpub': 1}, {'date_registered': '2018-08-24T06:56:05.171649', 'locale': 'en_US', 'full_name': 'Katwesige Wycliff', 'id': 'hxmsp', 'artpub': 1}, {'date_registered': '2018-08-24T07:03:07.113189', 'locale': 'en_US', 'full_name': 'Daniel Nyato', 'id': 'sv9n7', 'artpub': 1}, {'date_registered': '2018-08-18T13:53:09.046427', 'locale': 'en_US', 'full_name': 'Sheela Athreya', 'id': 'argec', 'artpub': 1}, {'date_registered': '2018-08-08T19:50:34.043407', 'locale': 'en_US', 'full_name': 'Wathela Alhassan', 'id': 'yd7kr', 'artpub': 1}, {'date_registered': '2018-07-30T19:35:50.311963', 'locale': 'en_US', 'full_name': 'Jean-Louis Bago', 'id': 'apdy8', 'artpub': 3}, {'date_registered': '2018-07-30T19:45:25.818780', 'locale': 'en_US', 'full_name': 'Miaba Louise Lompo', 'id': 'cykvw', 'artpub': 2}, {'date_registered': '2018-08-02T20:35:02.907939', 'locale': 'en_US', 'full_name': 'Aude E. A. Koutaba', 'id': 'cbvy3', 'artpub': 1}, {'date_registered': '2018-08-02T20:36:27.478646', 'locale': 'en_US', 'full_name': 'Aristide B. Valéa', 'id': '6jsge', 'artpub': 1}, {'date_registered': '2018-07-30T19:46:09.058941', 'locale': 'en_US', 'full_name': 'Wamadini dite Minata Souratié', 'id': '6427m', 'artpub': 1}, {'date_registered': '2018-07-23T10:36:29.372183', 'locale': 'en_US', 'full_name': 'Lauren Schroeder', 'id': '5u6wb', 'artpub': 1}, {'date_registered': '2017-10-27T10:38:55.163026', 'locale': 'en_US', 'full_name': 'OLADOKUN TAOFEEK ABIODUN', 'id': 'd5r9p', 'artpub': 1}, {'date_registered': '2018-07-21T21:17:38.900709', 'locale': 'en_US', 'full_name': 'Kolawole, Lucia Folasade', 'id': '5d6wv', 'artpub': 1}, {'date_registered': '2018-07-04T17:10:23.585256', 'locale': 'en_US', 'full_name': 'Mahmoud Bukar Maina', 'id': '36vmh', 'artpub': 1}, {'date_registered': '2018-07-04T18:37:15.518666', 'locale': 'en_US', 'full_name': 'Yunusa Mohammed Garba', 'id': '58gy7', 'artpub': 1}, {'date_registered': '2018-07-04T18:40:15.744906', 'locale': 'en_US', 'full_name': 'Ali Bukar Maina', 'id': '3rkzj', 'artpub': 1}, {'date_registered': '2018-07-04T18:42:11.616705', 'locale': 'en_US', 'full_name': 'Umar Ahmad', 'id': 'j9hq7', 'artpub': 1}, {'date_registered': '2018-07-04T18:43:50.470225', 'locale': 'en_US', 'full_name': 'Salihu Abubakar Tijjani', 'id': '4dfnx', 'artpub': 1}, {'date_registered': '2018-07-04T18:45:28.920913', 'locale': 'en_US', 'full_name': 'Ibrahim Harun Arrashid', 'id': 'kstng', 'artpub': 1}, {'date_registered': '2018-07-04T18:46:34.448103', 'locale': 'en_US', 'full_name': 'Muhammad Abdurrazak', 'id': 'y2mbv', 'artpub': 1}, {'date_registered': '2018-07-04T18:47:42.899848', 'locale': 'en_US', 'full_name': 'Hamidu Suleiman Kwairanga', 'id': 'fht36', 'artpub': 1}, {'date_registered': '2018-07-04T18:48:19.357435', 'locale': 'en_US', 'full_name': 'Aisha Umar Yaro', 'id': 'm6ufd', 'artpub': 1}, {'date_registered': '2018-07-04T18:49:06.748421', 'locale': 'en_US', 'full_name': 'Mosab Ali Awadelkareem', 'id': 'xrbd4', 'artpub': 1}, {'date_registered': '2018-06-29T17:12:38.078642', 'locale': 'en_US', 'full_name': 'Timar Samson GBAGUIDI', 'id': 'e5b6n', 'artpub': 1}]

app.layout = html.Div(children =
                    [
                     html.B(html.H1(children='AUTEURS :',style={'color': colors['text'],'textAlign': 'center'})),

                     dcc.Upload(children=[
                                        html.Form(children =[
                                                    dcc.Dropdown(
                                                        id='num',
                                                        options=[{'label':x['full_name'],'value':x['full_name']} for x in auth_data],
                                                ),
                                                    html.Table([
                                                        html.Tr([html.Td(['Full Name']), html.Td(id='name')]),
                                                        html.Tr([html.Td(['Id']), html.Td(id='id')]),
                                                        html.Tr([html.Td(["Nombre d'articles publies"]), html.Td(id='artpub')]),
                                                        html.Tr([html.Td(["date d'inscription"]), html.Td(id='registered')]),
                                                        html.Tr([html.Td(['Region']), html.Td(id='region')]),
                                                ])
                                            ])
                                        ],
                                style={
                                           'width': '100%',
                                           'height': '50px',
                                           'lineHeight': '50px',
                                           'borderWidth': '1px',
                                           'borderRadius': '5px',
                                           'textAlign': 'left',
                                           'margin-right': '200px',
                                           'margin-top': '0px'
                                        }
                                 )],
                style={'backgroundColor': '#2c3444'}

                )

@app.callback(
    [Output('name', 'children'),
     Output('id', 'children'),
     Output('artpub', 'children'),
     Output('registered', 'children'),
     Output('region', 'children')],
    [Input('num', 'value')])
def callback_a(x):
    k=0
    while k<len(auth_data) and x!=auth_data[k]['full_name']:
        k+=1
    if k<len(auth_data):
        return x,auth_data[k]['id'],auth_data[k]['artpub'], auth_data[k]['date_registered'],auth_data[k]['locale']
    else:
        return x,None,None,None,None

if __name__ == '__main__':
    app.run_server(debug=True)