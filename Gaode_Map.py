#高德API矩形区域检索
#由于限制
#author：hongsheng
#2019-03-31

import requests
import pandas as pd
import os
path =os.getcwd() +'/福建省'    #需手动添加省份
def Map_spider(city):

    data =[]
    for page_num in range(0, 100):
        r = requests.get('https://restapi.amap.com/v3/place/text?keywords=幼儿园&city='+city+'&output=json&offset=20&page='+str(page_num)+'&key=f0ea7d3e80ed429c80a5ab9ef4d24b2b')
        decodejson =r.json()
        print(decodejson)
        if decodejson['count'] != '0':
            for item in decodejson['pois']:
                print(item)
                name =item['name']
                address = item['address']
                lat_lng = item['location']
                if item['tel']== []:
                     tel ='暂无'
                else:
                    tel =item['tel']
            # if 'postcode' not in item:
            #     postcode ='暂无邮编'
            # else:
            #     postcode =item['postcode']
                province = item['pname']
                city = item['cityname']
                area = item['adname']
                if item['biz_ext']['rating'] == []:
                    rating ='暂无评分'
                else:
                    rating = item['biz_ext']['rating']
                if  item['photos'] == []:
                    picture = '暂无'
                else:
                    for key in item['photos']:
                        picture = key['url']
                data.append([name, tel ,address, lat_lng,  province, city, area, rating, picture])
        else:
            print('return 0')
            break
    df = pd.DataFrame(data, columns=['名称', '联系电话', '地址', '经纬度' ,  '省份', '城市', '区域',  '评分', '图片'])
    print(df)
    df.to_csv(path+'/'+city+'.csv', encoding='utf_8_sig', index=False, mode='a+')  # 写入csv文件



if __name__ == '__main__':
    citys =[ '厦门市','泉州市']    #需手动添加地级市

    for city in citys:
        Map_spider(city)
