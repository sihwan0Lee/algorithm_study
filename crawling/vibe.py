import time
import request
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.implicitly_wait(3)
url = 'https://vibe.naver.com/chart/total'

main_chart_image = []
ranking = []
music_image = []
music_name = []
lyricist = []
songwriter = []
arrangement = []
musician_image = []
musician_name = []
debut_date = []
music_genre = []
elbum_name = []
elbum_image = []
release_date = []
elbum_genre = []
elbum_descript = []
lyric = []

driver.get(url)

time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

mainimage = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.thumb > div > img')
for a in mainimage:
    main_chart_image.append(a.get_attribute('src'))

ranking100 = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.rank > span.text')
for b in ranking100:
    ranking.append(b.text)

driver.implicitly_wait(3)


links = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.song > div.title_badge_wrap > span > a')
musicnames = []
for link in links:
    musicnames.append(link.get_attribute('href'))

for musicname in musicnames:
    driver.get(musicname)
    musicpicture = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary_thumb > img')
    for c in musicpicture:
        music_image.append(c.get_attribute('src'))

    title = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary > div.text_area > h2 > span.title')
    for d in title:
        music_name.append(d.text[3:])

    lyric_ist = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary > div.text_area > div > div:nth-child(1)')
    # for e in lyric_ist:
    if len(lyric_ist) == 0:
        lyricist.append('')
    else:
        lyricist.append(lyric_ist[0].text[3:])

    song_writer = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary > div.text_area > div > div:nth-child(2)')

    if len(song_writer) == 0:
        songwriter.append('')
    else:
        songwriter.append(song_writer[0].text[3:])

    arrange_ment = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary > div.text_area > div > div:nth-child(3)')
    if len(arrange_ment) == 0:
        arrangement.append('')
    else:
        arrangement.append(arrange_ment[0].text[3:])

    driver.find_elements_by_css_selector('#content > div:nth-child(3) > a')

    gasa = driver.find_elements_by_css_selector(
        '#content > div:nth-child(3) > p')
    if len(gasa) == 0:
        lyric.append('')
    else:
        lyric.append(gasa[0].text)
       # lyric.append(gasa[0].text.replace('\n',''))
    print(lyric)

    musicianname = driver.find_elements_by_css_selector(
        '#content > div.summary_section > div.summary > div.text_area > h2 > span.sub_title > span:nth-child(2)')
    for f in musicianname:
        musician_name.append(f.text)
        print(musician_name)


# driver.back()
# time.sleep(3)
# driver.find_element_by_css_selector('#app > div > header > div.my_menu > div.ly_menu > div.menu_area > ul > li:nth-child(2) > a').send_keys(Keys.ENTER)
# time.sleep(3)
# driver.find_element_by_css_selector('#content > div:nth-child(2) > div > h3 > a > span').click()
# 가수 정보 부분
driver.get("https://vibe.naver.com/chart/total")

musicians = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.artist > span > span > span > a')
musician_info = []
for musician in musicians:
    musician_info.append(musician.get_attribute('href'))

# print(musician_info)
for info in musician_info:
    driver.get(info)
    musician_picture = driver.find_elements_by_css_selector(
        '#content > div.artist_summary_section > div.summary_thumb > img')
    for e in musician_picture:
        musician_image.append(e.get_attribute('src'))
        # print(musician_image)

    debutdate = driver.find_elements_by_css_selector(
        '#content > div.artist_summary_section > div.summary > div.text_area > h2 > span.sub_title > span')

    if len(debutdate) == 0:

        debut_date.append('')
    else:
        debut_date.append(debutdate[0].text)

    musiciangenre = driver.find_elements_by_css_selector(
        '#content > div.artist_summary_section > div.summary > div.text_area > h2 > span.sub_title')
    print(musiciangenre[0].text)
    if len(musiciangenre) == 0:
        music_genre.append('')
    else:
        music_genre.append(musiciangenre[0].text)

        # print(music_genre)

# 앨범 정보 부분
driver.get("https://vibe.naver.com/chart/total")

elbumname = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.album > a')
for x in elbumname:
    elbum_name.append(x.text)
    print(elbum_name)

elbums = driver.find_elements_by_css_selector(
    '#content > div.track_section > div:nth-child(1) > div > table > tbody > tr > td.album > a')
elbum_info = []
for elbum in elbums:
    elbum_info.append(elbum.get_attribute('href'))

for infom in elbum_info:
    driver.get(info)
    elbumimage = driver.find_elements_by_css_selector(
        '#content > div:nth-child(1) > div.summary_section > div.summary_thumb > img')
    for g in elbumimage:
        elbum_image.append(g.get_attribute('src'))
        print(elbum_image)

    releasedate = driver.find_elements_by_css_selector(
        '#content > div:nth-child(1) > div.summary_section > div.summary > div.text_area > div.sub > span:nth-child(1)')
    for h in releasedate:
        release_date.append(h.text)
        print(release_date)

    elbumgenre = driver.find_elements_by_css_selector(
        '#content > div:nth-child(1) > div.summary_section > div.summary > div.text_area > div.sub > span:nth-child(2)')
    for i in elbumgenre:
        elbum_genre.append(i.text)
        print(elbum_genre)

    descript = driver.find_elements_by_css_selector(
        '#content > div:nth-child(1) > div.summary_section > div.summary > div.text_area > div.info > div > span')
    if len(descript) == 0:
        elbum_descript.append('')
    else:
        elbum_descript.append(descript[0].text)
    print(elbum_descript)

vibe_top100 = [{
    'top100사진': props[0],
    '랭킹': props[1],
    '노래제목': props[2],
    '이미지(음악상세정보)': props[3],
    '작사': props[4],
    '작곡': props[5],
    '편곡': props[6],
    '가사': props[7],
    '가수이름': props[8],
    '가수사진': props[9],
    '데뷔일': props[10],
    '가수장르': props[11],
    '앨범이름': props[12],
    '앨범이미지': props[13],
    '발매일': props[14],
    '앨범장르': props[15],
    '앨범설명': props[16]
} for props in zip(main_chart_image, ranking, music_name, music_image, lyricist, songwriter, arrangement, lyric, musician_name, musician_image, debut_date, music_genre, elbum_name, elbum_image, release_date, elbum_genre, elbum_descript)]

with open('Vibetop_100mark4.csv', 'w')as csvfile:
    csvout = csv.DictWriter(csvfile, ['top100사진', '랭킹', '노래제목', '이미지(음악상세정보)', '작사', '작곡',
                                      '편곡', '가사', '가수이름', '가수사진', '데뷔일', '가수장르', '앨범이름', '앨범이미지', '발매일', '앨범장르', '앨범설명'])
    csvout.writeheader()
    csvout.writerows(vibe_top100)
