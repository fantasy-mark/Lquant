

```python
# -*- coding: utf-8 -*-
import tushare as ts
import datetime

Today = datetime.date.today().strftime('%Y-%m-%d')

# 获得行情数据,index为True时为大盘指数
df =ts.get_k_data(stock, index='True', start=Today, end=Today)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>open</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>volume</th>
      <th>code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>234</th>
      <td>2016-12-19</td>
      <td>3267.33</td>
      <td>3264.67</td>
      <td>3272.17</td>
      <td>3256.22</td>
      <td>153742399.0</td>
      <td>sh000002</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 获得实时盘口数据
ts.get_realtime_quotes(['600848']).T
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>name</th>
      <td>上海临港</td>
    </tr>
    <tr>
      <th>open</th>
      <td>18.500</td>
    </tr>
    <tr>
      <th>pre_close</th>
      <td>18.480</td>
    </tr>
    <tr>
      <th>price</th>
      <td>18.530</td>
    </tr>
    <tr>
      <th>high</th>
      <td>18.680</td>
    </tr>
    <tr>
      <th>low</th>
      <td>18.350</td>
    </tr>
    <tr>
      <th>bid</th>
      <td>18.540</td>
    </tr>
    <tr>
      <th>ask</th>
      <td>18.550</td>
    </tr>
    <tr>
      <th>volume</th>
      <td>3087732</td>
    </tr>
    <tr>
      <th>amount</th>
      <td>57170927.000</td>
    </tr>
    <tr>
      <th>b1_v</th>
      <td>11</td>
    </tr>
    <tr>
      <th>b1_p</th>
      <td>18.540</td>
    </tr>
    <tr>
      <th>b2_v</th>
      <td>5</td>
    </tr>
    <tr>
      <th>b2_p</th>
      <td>18.530</td>
    </tr>
    <tr>
      <th>b3_v</th>
      <td>189</td>
    </tr>
    <tr>
      <th>b3_p</th>
      <td>18.510</td>
    </tr>
    <tr>
      <th>b4_v</th>
      <td>41</td>
    </tr>
    <tr>
      <th>b4_p</th>
      <td>18.500</td>
    </tr>
    <tr>
      <th>b5_v</th>
      <td>564</td>
    </tr>
    <tr>
      <th>b5_p</th>
      <td>18.490</td>
    </tr>
    <tr>
      <th>a1_v</th>
      <td>412</td>
    </tr>
    <tr>
      <th>a1_p</th>
      <td>18.550</td>
    </tr>
    <tr>
      <th>a2_v</th>
      <td>89</td>
    </tr>
    <tr>
      <th>a2_p</th>
      <td>18.560</td>
    </tr>
    <tr>
      <th>a3_v</th>
      <td>63</td>
    </tr>
    <tr>
      <th>a3_p</th>
      <td>18.570</td>
    </tr>
    <tr>
      <th>a4_v</th>
      <td>99</td>
    </tr>
    <tr>
      <th>a4_p</th>
      <td>18.580</td>
    </tr>
    <tr>
      <th>a5_v</th>
      <td>145</td>
    </tr>
    <tr>
      <th>a5_p</th>
      <td>18.590</td>
    </tr>
    <tr>
      <th>date</th>
      <td>2016-12-19</td>
    </tr>
    <tr>
      <th>time</th>
      <td>15:00:00</td>
    </tr>
    <tr>
      <th>code</th>
      <td>600848</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 获得分笔明细
df = ts.get_today_ticks('601333')
df.head(10)
```

    [Getting data:]#ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    获取失败，请检查网络和URL
    [Getting data:]#ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    获取失败，请检查网络和URL
    [Getting data:]#ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    ElementTree not initialized, missing root
    获取失败，请检查网络和URL
    


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    <ipython-input-5-3c89eab1a016> in <module>()
    ----> 1 df = ts.get_today_ticks('601333')
          2 df.head(10)
    

    C:\Program Files\Anaconda3\lib\site-packages\tushare\stock\trading.py in get_today_ticks(code, retry_count, pause)
        252         else:
        253             return data
    --> 254     raise IOError(ct.NETWORK_URL_ERROR_MSG)
        255 
        256 
    

    OSError: 获取失败，请检查网络和URL



```python
# 获得大盘指数行情列表
df = ts.get_index()
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>code</th>
      <th>name</th>
      <th>change</th>
      <th>open</th>
      <th>preclose</th>
      <th>close</th>
      <th>high</th>
      <th>low</th>
      <th>volume</th>
      <th>amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000001</td>
      <td>上证指数</td>
      <td>-0.16</td>
      <td>3120.6963</td>
      <td>3122.9815</td>
      <td>3118.0846</td>
      <td>3125.2840</td>
      <td>3110.0817</td>
      <td>154169716</td>
      <td>1745.0024</td>
    </tr>
    <tr>
      <th>1</th>
      <td>000002</td>
      <td>Ａ股指数</td>
      <td>-0.16</td>
      <td>3267.3276</td>
      <td>3269.7467</td>
      <td>3264.6737</td>
      <td>3272.1723</td>
      <td>3256.2203</td>
      <td>153742399</td>
      <td>1741.8285</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000003</td>
      <td>Ｂ股指数</td>
      <td>-0.59</td>
      <td>347.2136</td>
      <td>346.7270</td>
      <td>344.6643</td>
      <td>347.2136</td>
      <td>344.4838</td>
      <td>427318</td>
      <td>3.1739</td>
    </tr>
    <tr>
      <th>3</th>
      <td>000008</td>
      <td>综合指数</td>
      <td>-0.36</td>
      <td>2718.7615</td>
      <td>2722.5028</td>
      <td>2712.7597</td>
      <td>2719.5762</td>
      <td>2706.1228</td>
      <td>34283078</td>
      <td>362.3441</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000009</td>
      <td>上证380</td>
      <td>0.26</td>
      <td>5559.2976</td>
      <td>5560.8822</td>
      <td>5575.0965</td>
      <td>5578.7082</td>
      <td>5543.6599</td>
      <td>37615901</td>
      <td>418.4614</td>
    </tr>
    <tr>
      <th>5</th>
      <td>000010</td>
      <td>上证180</td>
      <td>-0.41</td>
      <td>7270.7268</td>
      <td>7278.2749</td>
      <td>7248.1404</td>
      <td>7280.5392</td>
      <td>7239.1397</td>
      <td>56185766</td>
      <td>560.8394</td>
    </tr>
    <tr>
      <th>6</th>
      <td>000011</td>
      <td>基金指数</td>
      <td>-0.13</td>
      <td>5744.4351</td>
      <td>5745.1045</td>
      <td>5737.6042</td>
      <td>5745.6978</td>
      <td>5733.1554</td>
      <td>16142759</td>
      <td>421.3481</td>
    </tr>
    <tr>
      <th>7</th>
      <td>000012</td>
      <td>国债指数</td>
      <td>-0.01</td>
      <td>159.6262</td>
      <td>159.5861</td>
      <td>159.5738</td>
      <td>159.6560</td>
      <td>159.5421</td>
      <td>724217</td>
      <td>7.3236</td>
    </tr>
    <tr>
      <th>8</th>
      <td>000016</td>
      <td>上证50</td>
      <td>-0.47</td>
      <td>2299.7136</td>
      <td>2302.3152</td>
      <td>2291.3842</td>
      <td>2303.6854</td>
      <td>2288.3022</td>
      <td>24162297</td>
      <td>239.9928</td>
    </tr>
    <tr>
      <th>9</th>
      <td>000017</td>
      <td>新综指</td>
      <td>-0.15</td>
      <td>2634.0751</td>
      <td>2636.0274</td>
      <td>2631.9883</td>
      <td>2638.0382</td>
      <td>2625.1682</td>
      <td>152506868</td>
      <td>1723.7991</td>
    </tr>
    <tr>
      <th>10</th>
      <td>000300</td>
      <td>沪深300</td>
      <td>-0.51</td>
      <td>3342.3449</td>
      <td>3346.0305</td>
      <td>3328.9827</td>
      <td>3344.8584</td>
      <td>3324.9986</td>
      <td>81640678</td>
      <td>860.9569</td>
    </tr>
    <tr>
      <th>11</th>
      <td>000905</td>
      <td>中证500</td>
      <td>0.03</td>
      <td>6319.8574</td>
      <td>6318.5239</td>
      <td>6320.7324</td>
      <td>6330.3823</td>
      <td>6297.3666</td>
      <td>62579158</td>
      <td>701.8056</td>
    </tr>
    <tr>
      <th>12</th>
      <td>399001</td>
      <td>深证成指</td>
      <td>-0.50</td>
      <td>10330.6100</td>
      <td>10334.7570</td>
      <td>10283.1640</td>
      <td>10330.6100</td>
      <td>10262.6880</td>
      <td>15843201398</td>
      <td>2251.1279</td>
    </tr>
    <tr>
      <th>13</th>
      <td>399002</td>
      <td>深成指R</td>
      <td>-0.50</td>
      <td>12203.9200</td>
      <td>12208.8180</td>
      <td>12147.8700</td>
      <td>12203.9200</td>
      <td>12123.6800</td>
      <td>6556349056</td>
      <td>804.9444</td>
    </tr>
    <tr>
      <th>14</th>
      <td>399003</td>
      <td>成份Ｂ指</td>
      <td>-0.78</td>
      <td>6175.2720</td>
      <td>6181.4180</td>
      <td>6133.4370</td>
      <td>6186.9140</td>
      <td>6133.4370</td>
      <td>10470891</td>
      <td>0.7977</td>
    </tr>
    <tr>
      <th>15</th>
      <td>399004</td>
      <td>深证100R</td>
      <td>-0.81</td>
      <td>4533.2390</td>
      <td>4537.1430</td>
      <td>4500.4960</td>
      <td>4533.2390</td>
      <td>4492.5420</td>
      <td>2501991809</td>
      <td>308.6945</td>
    </tr>
    <tr>
      <th>16</th>
      <td>399005</td>
      <td>中小板指</td>
      <td>-0.44</td>
      <td>6543.8380</td>
      <td>6543.1840</td>
      <td>6514.0970</td>
      <td>6547.3230</td>
      <td>6506.6710</td>
      <td>1023477597</td>
      <td>156.0036</td>
    </tr>
    <tr>
      <th>17</th>
      <td>399006</td>
      <td>创业板指</td>
      <td>-0.89</td>
      <td>1995.0030</td>
      <td>1998.1130</td>
      <td>1980.4100</td>
      <td>1995.0030</td>
      <td>1976.7700</td>
      <td>629146748</td>
      <td>113.4235</td>
    </tr>
    <tr>
      <th>18</th>
      <td>399008</td>
      <td>中小300</td>
      <td>-0.36</td>
      <td>1439.5080</td>
      <td>1439.6470</td>
      <td>1434.4530</td>
      <td>1439.7780</td>
      <td>1432.1430</td>
      <td>3024388905</td>
      <td>389.1737</td>
    </tr>
    <tr>
      <th>19</th>
      <td>399100</td>
      <td>新 指 数</td>
      <td>-0.32</td>
      <td>8684.7830</td>
      <td>8688.4650</td>
      <td>8660.3400</td>
      <td>8684.7830</td>
      <td>8640.7150</td>
      <td>15547638506</td>
      <td>2224.9370</td>
    </tr>
    <tr>
      <th>20</th>
      <td>399101</td>
      <td>中小板综</td>
      <td>-0.27</td>
      <td>11558.4210</td>
      <td>11564.1660</td>
      <td>11532.7100</td>
      <td>11559.5680</td>
      <td>11510.9390</td>
      <td>6338526071</td>
      <td>934.0692</td>
    </tr>
    <tr>
      <th>21</th>
      <td>399106</td>
      <td>深证综指</td>
      <td>-0.38</td>
      <td>1990.8030</td>
      <td>1991.6350</td>
      <td>1984.1010</td>
      <td>1990.8030</td>
      <td>1979.5610</td>
      <td>15843201398</td>
      <td>2251.1279</td>
    </tr>
    <tr>
      <th>22</th>
      <td>399107</td>
      <td>深证Ａ指</td>
      <td>-0.38</td>
      <td>2082.6380</td>
      <td>2083.5130</td>
      <td>2075.6300</td>
      <td>2082.6380</td>
      <td>2070.8540</td>
      <td>15818453212</td>
      <td>2249.5239</td>
    </tr>
    <tr>
      <th>23</th>
      <td>399108</td>
      <td>深证Ｂ指</td>
      <td>-0.36</td>
      <td>1134.2460</td>
      <td>1134.2240</td>
      <td>1130.0900</td>
      <td>1134.3430</td>
      <td>1129.0110</td>
      <td>24748186</td>
      <td>1.6040</td>
    </tr>
    <tr>
      <th>24</th>
      <td>399333</td>
      <td>中小板R</td>
      <td>-0.44</td>
      <td>7148.1540</td>
      <td>7147.4390</td>
      <td>7115.6670</td>
      <td>7151.9600</td>
      <td>7107.5550</td>
      <td>1023477597</td>
      <td>156.0036</td>
    </tr>
    <tr>
      <th>25</th>
      <td>399606</td>
      <td>创业板R</td>
      <td>-0.89</td>
      <td>2064.1000</td>
      <td>2067.3170</td>
      <td>2049.0010</td>
      <td>2064.1000</td>
      <td>2045.2340</td>
      <td>629146748</td>
      <td>113.4235</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 获得大单交易数据
df = ts.get_sina_dd('600848', date='2016-12-19') #默认400手
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>code</th>
      <th>name</th>
      <th>time</th>
      <th>price</th>
      <th>volume</th>
      <th>preprice</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>600848</td>
      <td>上海临港</td>
      <td>14:54:28</td>
      <td>18.55</td>
      <td>45735</td>
      <td>18.53</td>
      <td>买盘</td>
    </tr>
    <tr>
      <th>1</th>
      <td>600848</td>
      <td>上海临港</td>
      <td>10:26:56</td>
      <td>18.60</td>
      <td>50000</td>
      <td>18.56</td>
      <td>买盘</td>
    </tr>
    <tr>
      <th>2</th>
      <td>600848</td>
      <td>上海临港</td>
      <td>10:20:42</td>
      <td>18.60</td>
      <td>82100</td>
      <td>18.56</td>
      <td>买盘</td>
    </tr>
    <tr>
      <th>3</th>
      <td>600848</td>
      <td>上海临港</td>
      <td>10:11:51</td>
      <td>18.55</td>
      <td>50000</td>
      <td>18.54</td>
      <td>买盘</td>
    </tr>
    <tr>
      <th>4</th>
      <td>600848</td>
      <td>上海临港</td>
      <td>10:09:24</td>
      <td>18.55</td>
      <td>43321</td>
      <td>18.56</td>
      <td>卖盘</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
