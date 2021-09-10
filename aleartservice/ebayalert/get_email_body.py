import os
import json
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

from django.conf import settings


def get_search_items_list(search_pharse):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # sample_json_path = os.path.join(dir_path, 'data', 'sample_res.json')
    # with open(sample_json_path,'r') as f:
    #     output = json.loads(f.read())
    # return output['itemSummaries']


    try:
        api = Finding(appid=settings.EBAY_APP_ID, config_file=None)
        response = api.execute('findItemsAdvanced', {'keywords': search_pharse})
        search_results = response.reply.searchResult
        item_summary = []
        if hasattr(search_results, "item"):
            items = response.reply.searchResult.item
        else:
            return item_summary
        sorted_items = sorted(items, key=lambda x: float(x.sellingStatus.currentPrice.value))
        for item in sorted_items[0:20]:
            info_dict = {}
            info_dict['itemId'] = item.itemId
            info_dict['title'] = item.title
            info_dict['price'] = {"currency": item.sellingStatus.currentPrice._currencyId, 
                                  "value": item.sellingStatus.currentPrice.value}
            info_dict['itemWebUrl'] = item.viewItemURL
            item_summary.append(info_dict)
        return item_summary
    except ConnectionError as e:
        raise RuntimeError(e)


def get_search_items_body(search_pharse, item_summary):
    if item_summary:
        html_content = 'Search Results for %s <br><br>' % search_pharse
        html_content += '''<table style='border:1px solid gray;
                border-collapse:collapse;'>
                <tr>
                    <th style='border:1px solid gray;border-collapse:collapse;
                        padding:5px;'>Item Title</th>
                    <th style='border:1px solid gray;border-collapse:collapse;
                        padding:5px;text-align:left;'>Price</th>
                    <th style='border:1px solid gray;border-collapse:collapse;
                        padding:5px;'>Book Now</th>
                </tr>'''
        for item in item_summary:
            html_content += '''<tr>
            <td style='border:1px solid gray;border-collapse:collapse;
                padding:5px;'>%s</td>
            <td style='border:1px solid gray;border-collapse:collapse;
                padding:5px;'>%s</td>
            <td style='border:1px solid gray;border-collapse:collapse;
                padding:5px;'><a href="%s">Book Now</a></td></tr>''' % (
            item['title'],
            item['price']['value'] + ' ' + item['price']['currency'],
            item['itemWebUrl'])
        html_content += "</table>"
    else:
        html_content = 'No exact matches found'
    return html_content