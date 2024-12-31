import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
# 선수들 정보, 샷차트, 클러치 타임 관련 정보 가져오는 모듈
from nba_api.stats.static import players
from nba_api.stats.endpoints import ShotChartDetail
from nba_api.stats.endpoints import playerdashboardbyclutch as pc

st.markdown('# NBA ANALYSIS')
st.markdown('#### -->모든 정보는 현시즌의 정보이며, 계속 최신화 됩니다.')

# 함수 선언
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 최근 5일간 팀에서 제일 핫한 선수들 수집
@st.cache_data #다시 실행할 때 이거는 다시 안해도 돼 !
def crawling_hot_player():
    # #브라우저 열기
    # browser = webdriver.Chrome()

    # # 빈 리스트 생성
    # results_hot_player = []
    # # 현재 시각 가져오기
    # current_date = datetime.now()
    # # 18시간 빼기
    # adjusted_date = current_date - timedelta(hours=18)

    # year = adjusted_date.year
    # month = adjusted_date.month
    # day = adjusted_date.day
    # today = int(f'{year}{month}{day}')
    # # """최근 5일 경기중 팀중에서 제일 핫한 선수들 수집"""
    # date = [today-1,today-2,today-3,today-4,today-5]
    # # 정보수집
    # for i in date:
    #     url = f'https://www.cbssports.com/nba/scoreboard/{i}/'
    #     browser.get(url)
    #     time.sleep(1)

    #     soup = BeautifulSoup(browser.page_source, 'html.parser')

    #     today_game_list = soup.select('div.score-card-container > div > div > div.live-update')

    #     for game_list in today_game_list:
    #         date = soup.select('#ToggleContainer-buttons-button-2 > a')[0].text.strip()
    #         game_list = game_list.select('div.section.team-player-stats.basketball > table > tbody >tr')
    #         for i in range(len(game_list)):
    #             best_player = game_list[i]
    #             name = best_player.select('span > a')[0].text
    #             team = best_player.select('span.player-team')[0].text
    #             position = best_player.select('span.player-position')[0].text
    #             stat = best_player.select('span')[3].text.split(',')
    #             if(len(stat) == 1):
    #                 PTS = stat[0].strip()[:-4]
    #             if(len(stat) == 2):
    #                 PTS = stat[0].strip()[:-4]
    #                 REB = stat[1].strip()[:-4]
    #             elif(len(stat) == 3):
    #                 PTS = stat[0].strip()[:-4]
    #                 REB = stat[1].strip()[:-4]
    #                 AST = stat[2].strip()[:-4]
    #             data = [date, name, team, position, PTS, REB, AST]
    #             results_hot_player.append(data)
    # df_hot_player = pd.DataFrame(results_hot_player)
    # df_hot_player.columns = ['date', 'player', 'team', 'position' ,'PTS', 'REB', 'AST']
    # browser.close()
    
    df_hot_player = pd.read_csv('./hot_players.csv')

    return df_hot_player

# 현재 부상으로 뛰지 못하는 선수들 수집
@st.cache_data
def crawling_injury_player():
    # browser = webdriver.Chrome()
    # url = 'https://www.cbssports.com/nba/injuries/'
    # browser.get(url)
    # time.sleep(1)
    # soup = BeautifulSoup(browser.page_source, 'html.parser')

    # injury_player_results = []
    # injury_data_list = soup.select('div.TableBaseWrapper')

    # for injury_data in injury_data_list:
    #     team = injury_data.select('span.TeamName > a')[0].text
    #     for i in range(len(injury_data.select('tbody > tr'))):
    #         injury_p = injury_data.select('tbody > tr')[i]
    #         name = injury_p.select('span.CellPlayerName--long > span > a')[0].text
    #         position = injury_p.select('td.TableBase-bodyTd')[1].text.strip()
    #         update_date = injury_p.select('td.TableBase-bodyTd')[2].text.strip()
    #         injury = injury_p.select('td.TableBase-bodyTd')[3].text.strip()
    #         injury_status = injury_p.select('td.TableBase-bodyTd')[4].text.strip()
            
    #         data = [team, name, position, update_date, injury, injury_status]
    #         injury_player_results.append(data)
    # df_injury_player = pd.DataFrame(injury_player_results)
    # df_injury_player.columns = ['team', 'player', 'position' ,'update_date', 'injury', 'injury_status']
    # browser.close()

    df_injury_player = pd.read_csv('./injury_player.csv')

    return df_injury_player 

# 올해 시즌 선수들의 연봉 수집
@st.cache_data
def crawling_players_salaries():
    # browser = webdriver.Chrome()
    # url = 'https://hoopshype.com/salaries/players/'
    # browser.get(url)
    # time.sleep(1)
    # soup = BeautifulSoup(browser.page_source, 'html.parser')

    # player_name_list = soup.select('div.table-wrapper > div.pinned > table > tbody > tr')

    # results_sal = []

    # for player_name in player_name_list:    
    #     name = player_name.select('td.name > a')[0].text.strip()
    #     salaries = player_name.select('td.hh-salaries-sorted')[0].text.replace(',', '').strip()[1:]
    #     data = [name, salaries]
    #     results_sal.append(data)
    # df_sal = pd.DataFrame(results_sal)
    # df_sal.columns = ['name', 'salaries($)']
    # df_sal['salaries($)'] = df_sal['salaries($)'].astype(int)
    # browser.close()
    df_sal = pd.read_csv('./player_salaries.csv')

    return df_sal

# 올해 시즌 경기를 출전한 선수들의 여러가지 스텟 수집
@st.cache_data
def crawling_players_stats():
    browser = webdriver.Chrome()
    url = 'https://www.espn.com/nba/stats/player'
    browser.get(url)
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # 선수 명단 끝까지 확인하기
    while True:
        # 'show more' 버튼의 존재 여부를 확인
        page_btns = browser.find_elements('css selector', 'a.AnchorLink.loadMore__link')
        
        # page_btns 리스트가 비어 있지 않다면 (즉, 하나 이상의 'show more' 버튼이 존재한다면)
        if page_btns:
            # 첫 번째 'show more' 버튼을 클릭
            page_btns[0].click()
            # 페이지가 새로운 컨텐츠를 불러오고 렌더링할 시간을 주기 위해 대기
            time.sleep(0.5)
            # BeautifulSoup 객체를 업데이트
            soup = BeautifulSoup(browser.page_source, 'html.parser')
        else:
            # 'show more' 버튼이 없으면 while 루프를 빠져나옴
            break
    # 데이터가 나눠져 있어서 두번 따로 리스트에 담고 데이터 프레임으로 만들어서 합치기
    results_1 = []
    results_2 = []

    player_name_list = soup.select('div.flex > table > tbody.Table__TBODY > tr')
    for player_name in player_name_list:
        name = player_name.select('a.AnchorLink')[0].text
        team = player_name.select('span')[0].text
        
        data = [name, team]
        results_1.append(data)
    df1 = pd.DataFrame(results_1)
    df1.columns = ['NAME', 'TEAM']

    player_stat_list = soup.select('div.Table__Scroller> table > tbody.Table__TBODY > tr')
    for player_stat in player_stat_list:
        data = []
        for i in range(len(player_stat('td'))):
            element = player_stat('td')[i].text.strip()
            data.append(element)
        results_2.append(data)
    df2 = pd.DataFrame(results_2)
    df2.columns = ['POS', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'DD2', 'TD3']
    # result1과 result2 합치기
    df_player_stat = pd.concat([df1, df2], axis =1)
    df_player_stat.iloc[:, 3:22] = df_player_stat.iloc[:, 3:22].astype(float)
    browser.close()

    return df_player_stat

# 현역 선수들의 이름과 ID 수집
@st.cache_data
def read_player_name_id():
    # NBA 선수 리스트 불러오기
    players_dict = players.get_players()
    player_name = []
    player_id = []
    # 현재 뛰고 있는 선수만 추출
    for player in players_dict:
        if player['is_active'] == True:
            player_name.append(player['full_name'])
            player_id.append(player['id'])
    # 선수 이름과 선수 아이디 데이터프레임으로 만들기
    df_player_name_id = pd.DataFrame([player_name, player_id]).transpose()
    df_player_name_id.columns = ['NAME', 'ID']

    return df_player_name_id

# nba_api 라이브러리를 이용하여 클러치 상황에서의 선수들의 데이터를 추출
def get_clutch_data(player_id_list):
    clutch_data_list = []

    for player_id in player_id_list:
        data = pc.PlayerDashboardByClutch(player_id=player_id, season_type_playoffs='Regular Season',season = '2023-24')
        clutch_data_t = data.nba_response.get_data_sets()
        # 4쿼터 경기 5분, 3분, 1분 전 상대팀과 점수차 5점 이내인 상황만 추출
        cmin5 = clutch_data_t['Last5MinPlusMinus5PointPlayerDashboard']['data'][0]
        cmin3 = clutch_data_t['Last3MinPlusMinus5PointPlayerDashboard']['data'][0]
        cmin1 = clutch_data_t['Last1MinPlusMinus5PointPlayerDashboard']['data'][0]

        df = pd.DataFrame([cmin5, cmin3, cmin1]).transpose()
        df.index = clutch_data_t['Last1MinPlusMinus5PointPlayerDashboard']['headers']
        df.columns = df.iloc[0]  # 이 부분은 첫 번째 행을 열 이름으로 설정
        df = df.iloc[1:]  # 첫 번째 행을 제거
        clutch_data_list.append(df)
    return clutch_data_list

# 데이터 출력
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

df_hot_player = crawling_hot_player()
st.markdown('#### 1.최근 5일 경기중 팀중에서 제일 핫한 선수들')
with st.expander("데이터 보기"):
    st.dataframe(df_hot_player)

df_injury_player = crawling_injury_player()
st.markdown('#### 2.현재 부상으로 뛰지 못하는 선수들')
with st.expander("데이터 보기"):
    st.dataframe(df_injury_player)

df_player_name_id = read_player_name_id()
# 선수 풀 네임을 쉽게 가져오기 위해서 사이드바로 선수 리스트 삽입
with st.sidebar:
    word = st.text_input("선수명을 입력하세요")

    cond = df_player_name_id['NAME'].str.contains(word)
    df_player_name_id['ID'] = df_player_name_id['ID'].astype(str)
    st.dataframe(df_player_name_id[cond])
# 선수들 스텟 정보 가져오기
df_player_stat = crawling_players_stats()
# 선수들 연봉 정보 가져오기
df_player_salaries = crawling_players_salaries()

# 입력값 받아서 분석한 것 출력
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 선수 아이디를 통해서 선수가 많이 시도하는 슛 위치 파악
#########################################################################################

st.markdown('#### 3.선수의 슛 스팟, 스텟 분석')
player_id_num = st.text_input("선수 ID 을 입력하세요")

try:
    chosen_player = df_player_name_id[df_player_name_id['ID'] == player_id_num].iloc[0,0]
except:
    pass

columns = st.columns(3)

with columns[0]:
    try:
        st.markdown('#### 이번 시즌 슛 시도')
        shot_char_detail_dfs = ShotChartDetail(team_id = '0', player_id = player_id_num, 
                                            season_nullable = '2023-24',  context_measure_simple = 'FGM').get_data_frames()[0]
        fig, ax = plt.subplots()
        sns.scatterplot(x = 'LOC_X', y = 'LOC_Y', data = shot_char_detail_dfs.loc[shot_char_detail_dfs['SHOT_DISTANCE']>=24], 
                        color = 'blue', label = '3Point', ax=ax)
        sns.scatterplot(x = 'LOC_X', y = 'LOC_Y', data = shot_char_detail_dfs.loc[shot_char_detail_dfs['SHOT_DISTANCE']<24], 
                        color = 'red', label = '2Point', ax=ax)
        # y축 범위 설정
        plt.xlim(-250, 250)
        plt.ylim(0, 500)
        st.pyplot(fig)
    except:
        pass
with columns[1]:
    try:
        st.markdown('#### 이번 시즌 슛 성공')
        fig, ax = plt.subplots()
        sns.scatterplot(x = 'LOC_X', y = 'LOC_Y', data = shot_char_detail_dfs[shot_char_detail_dfs['SHOT_MADE_FLAG'] == 1].loc[shot_char_detail_dfs['SHOT_DISTANCE']>=24], 
                        color = 'blue', label = '3Point', ax=ax)
        sns.scatterplot(x = 'LOC_X', y = 'LOC_Y', data = shot_char_detail_dfs[shot_char_detail_dfs['SHOT_MADE_FLAG'] == 1].loc[shot_char_detail_dfs['SHOT_DISTANCE']<24], 
                        color = 'red', label = '2Point', ax=ax)
        # y축 범위 설정
        plt.xlim(-250, 250)
        plt.ylim(0, 500)
        st.pyplot(fig)
    except:
        pass
with columns[2]:
    try:
        columns_1 = st.columns(2)
        with columns_1[0]:
            st.metric("득점(평균)", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'PTS'].iloc[0].astype(float))
        with columns_1[1]:    
            st.metric("투입 시간(평균)", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'MIN'].iloc[0].astype(float))
        columns_2 = st.columns(2)
        with columns_1[0]:
            st.metric("경기당 슛성공", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'FGM'].iloc[0].astype(float))
        with columns_1[1]:
            st.metric("턴오버(평균)", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'TOV'].iloc[0].astype(float))
        columns_2 = st.columns(2)
        with columns_1[0]:
            st.metric("슛성공률(평균)", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'FG%'].iloc[0].astype(float))
        with columns_1[1]:
            st.metric("3점슛 성공률", value = df_player_stat.loc[df_player_stat['NAME'] == chosen_player,'3P%'].iloc[0].astype(float))
    except:
        pass

# 선수 아이디를 통해서 경기 종료 5분,3분,1분 전에서의 승률과 슛 성공률 분석
#######################################################################################
st.markdown("#### 4.입력받은 3명의 선수에 대한 경기 종료 5분전, 3분전, 1분전 승률/슛 성공률 비교")
st.markdown("##### 상대팀과의 점수 차이가 +/- 5점 이내인 경우")
# 3명의 선수 ID 입력 받기
player_id1 = st.text_input("선수 ID 1을 입력하세요")
player_id2 = st.text_input("선수 ID 2을 입력하세요")
player_id3 = st.text_input("선수 ID 3을 입력하세요")
try:
    player_id_list = [player_id1, player_id2, player_id3]
    player_name_1 = df_player_name_id[df_player_name_id['ID'] == player_id1]['NAME'].iloc[0]
    player_name_2 = df_player_name_id[df_player_name_id['ID'] == player_id2]['NAME'].iloc[0]
    player_name_3 = df_player_name_id[df_player_name_id['ID'] == player_id3]['NAME'].iloc[0]
except:
    pass

columns = st.columns(2)
with columns[0]:
    try:
        st.markdown('#### 3명의 선수의 클러치 타임 승률')
        clutch_data = get_clutch_data(player_id_list)
        # 선수별 승률 데이터를 가져오기
        Player_1_W_PCT = clutch_data[0].loc['W_PCT']
        Player_2_W_PCT = clutch_data[1].loc['W_PCT']
        Player_3_W_PCT = clutch_data[2].loc['W_PCT']
        # 승률 데이터를 바탕으로 새로운 데이터프레임을 생성하기
        W_PCT_df = pd.DataFrame({ 
            player_name_1: Player_1_W_PCT.tolist(), # Series 타입을 리스트 타입으로 변환
            player_name_2: Player_2_W_PCT.tolist(),
            player_name_3: Player_3_W_PCT.tolist()
        }, index=Player_1_W_PCT.index)

        # 새로운 그래프를 생성
        fig, ax = plt.subplots()
        # 데이터프레임의 데이터로 그래프 그리기
        W_PCT_df.plot(kind='bar', ax=ax)
        ax.set_title('Win Percentage in Clutch Time')
        ax.set_xlabel('Left Minute')
        ax.set_ylabel('Win Percentage')
        ax.legend(title='Player')
        # x축 라벨을 가로로 설정합니다.
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
        st.pyplot(fig)
    except:
        pass
with columns[1]:
    try:
        st.markdown('#### 클러치 타임 슛 성공률')
        clutch_data = get_clutch_data(player_id_list)
        # 선수별 슛 성공률 데이터를 가져오기
        Player_1_FG_PCT = clutch_data[0].loc['FG_PCT']
        Player_2_FG_PCT = clutch_data[1].loc['FG_PCT']
        Player_3_FG_PCT = clutch_data[2].loc['FG_PCT']
        # 슛 성공률 데이터를 바탕으로 새로운 데이터프레임을 생성합니다.
        FG_PCT_df = pd.DataFrame({
            player_name_1: Player_1_FG_PCT.tolist(),
            player_name_2: Player_2_FG_PCT.tolist(),
            player_name_3: Player_3_FG_PCT.tolist()
        }, index=Player_1_FG_PCT.index)

        # 새로운 그래프를 생성
        fig, ax = plt.subplots()
        # 데이터프레임의 데이터로 그래프 그리기
        FG_PCT_df.plot(kind='bar', ax=ax)
        ax.set_title('Feild Goal Percentage in Clutch Moments')
        ax.set_xlabel('Left Minute')
        ax.set_ylabel('Field Goal Percentage')
        ax.legend(title='Player')
        # x축 라벨을 가로로 설정합니다.
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
        st.pyplot(fig)
    except:
        pass

# 선수 분석과 포지션별 수비활동지수 공격활동지수를 파악하여 어느포자션이 게임 승리에 많은 영향을 끼치는지 파악
# 어떤 선수가 연봉대비 효율이 어떠한지 파악
##################################################################################
# 현 시즌 선수들의 스텟 보기
st.markdown('#### 5.현시즌 선수들의 평균경기스텟')
with st.expander("데이터 보기"):
    st.dataframe(df_player_stat)

# 공격 유효 점수, 수비 유효 점수 새로운 컬럼 추가
df_player_stat['Offense_score'] = df_player_stat['PTS'] +df_player_stat['FG%']+df_player_stat['AST'] +df_player_stat['STL']
df_player_stat['Defense_score'] = df_player_stat['REB'] +df_player_stat['BLK']+ df_player_stat['STL']

classify_data = df_player_stat[df_player_stat['MIN'] > 15]


st.markdown('#### 6.포지션별 평균 공/수 유효 점수 파악')
st.markdown('###### 포지션별 데이터를 분석하기 앞서 평균 출전 시간이 15분 미만인 선수는 제외 후 분석하였습니다.')
columns = st.columns(2)
with columns[0]:
    # 새로운 그래프를 생성
    fig, ax = plt.subplots()
    # 데이터프레임의 데이터로 그래프 그리기
    sns.barplot(ax = ax,x='POS',y='Offense_score',data = classify_data, palette = 'pastel')
    st.pyplot(fig)
with columns[1]:
    # 새로운 그래프를 생성
    fig, ax = plt.subplots()
    # 데이터프레임의 데이터로 그래프 그리기
    sns.barplot(ax = ax,x='POS',y='Defense_score',data = classify_data, palette = 'pastel')
    st.pyplot(fig)

df_player_salaries['salaries($)'] = df_player_salaries['salaries($)'] / 1000

# 수평 막대 그래프 사용
st.markdown('#### 7.공격 활동 지수 TOP 상위 선수 10명')
best_offense_players = classify_data.groupby(['NAME','TEAM']).agg({'Offense_score':'max'}).sort_values(by='Offense_score',ascending = False).head(10)
fig, ax = plt.subplots()
best_offense_players.plot(kind = 'barh',color = 'lightcoral',figsize=(10,5), title = 'best offense players', ax = ax)
st.pyplot(fig)

# 상위 선수들의 연봉 수치 표시
best_offense_players = best_offense_players.reset_index()
p_f_results = []
for i in best_offense_players['NAME'].values:
    try:
        salaries = df_player_salaries.loc[df_player_salaries['name'] == i,'salaries($)'].iloc[0].astype(int)
    except:
        salaries = 0
    p_f_results.append([i, salaries])
    
p_o_df = pd.DataFrame(p_f_results)
p_o_df = p_o_df.set_index(0)
fig, ax = plt.subplots()
p_o_df.plot(kind = 'barh',color = 'lightskyblue',figsize=(10,5), title = 'best offense players salaries', ax = ax, xlabel= 'X1000dollars', ylabel='player')
ax.legend(labels=['player_salaries'])
st.pyplot(fig)


# 수평 막대 그래프 사용
st.markdown('#### 8.수비 활동 지수 TOP 상위 선수 10명')
best_defense_players = classify_data.groupby(['NAME','TEAM']).agg({'Defense_score':'max'}).sort_values(by='Defense_score',ascending = False).head(10)
fig, ax = plt.subplots()
best_defense_players.plot(kind = 'barh',color = 'lightcoral',figsize=(10,5),title = 'best defense players', ax = ax)
st.pyplot(fig)

# 상위 선수들의 연봉 수치 표시
best_defense_players = best_defense_players.reset_index()
p_d_results = []
for i in best_defense_players['NAME'].values:
    salaries = df_player_salaries.loc[df_player_salaries['name'] == i,'salaries($)'].iloc[0].astype(int)
    p_d_results.append([i, salaries])
    
p_d_df = pd.DataFrame(p_d_results)
p_d_df = p_d_df.set_index(0)
fig, ax = plt.subplots()
p_d_df.plot(kind = 'barh',color = 'lightskyblue',figsize=(10,5), title = 'best defense players salaries', ax = ax, xlabel= 'X1000dollars',  ylabel='player')
ax.legend(labels=['player_salaries'])
st.pyplot(fig)

st.markdown('#### 9.선수 효율 점수와 연봉 분석')
player_id_num_2 = st.text_input("선수 아이디를 입력하세요")

try:
    Chosen_player_name = df_player_name_id[df_player_name_id['ID'] == player_id_num_2]['NAME'].iloc[0]
except:
    pass

columns = st.columns(3)
with columns[0]:
    try:
        st.metric('##### 공격 효율 점수', value = df_player_stat.loc[df_player_stat['NAME'] == Chosen_player_name,'Offense_score'].iloc[0].astype(int))

    except:
        pass
with columns[1]:
    try:
        st.metric('##### 수비 효율 점수', value = df_player_stat.loc[df_player_stat['NAME'] == Chosen_player_name,'Defense_score'].iloc[0].astype(int))
    except:
        pass
with columns[2]:
    try:
        st.metric('##### 연봉 (X1000dollar)', value = df_player_salaries.loc[df_player_salaries['name'] == Chosen_player_name,'salaries($)'].iloc[0].astype(int))
    except:
        pass

@st.cache_data
def explanation():
    st.markdown('### 타겟 대상')
    st.markdown('###### NBA 구단(LA_LAKERS) / DATA ANALYST(데이터분석가)')
    st.markdown('###### KBL 구단(SK_NIGHTS) / 전력분석팀')
    st.markdown('###### KBL / 데이터분석가')

    st.markdown('### 사용방법')
    st.markdown('###### SIDE> 좌측 사이드바에서 선수 이름을 검색하여 검색하고 싶은 선수의 ID를 확인합니다. ')
    st.markdown('###### 3번. 첫 번째 칸에 검색하고 싶은 선수의 ID를 입력합니다.')
    st.markdown('###### --> 선수의 슛 시도 위치와 성공한 위치 정보, 스텟을 출력합니다.')
    st.markdown('###### --> 선수의 기록이 없다면 그래프가 출력되지 않습니다.')
    st.markdown('###### 4번. 클러치 타임에서의 정보를 알고 싶은 3명의 선수의 아이디를 입력합니다.')
    st.markdown('###### --> 3명의 선수의 5,3,1분전 상황에서의 승률, 슛 성공률이 출력됩니다.')
    st.markdown('###### --> 클러치 상황에서의 정보가 부족한 경우 그래프가 나오지 않을 수 있습니다.')
    st.markdown('###### --> 클러치 상황에서의 정보가 많은 선수를 입력하는 것을 추천합니다.')
    st.markdown('###### 9번. 입력칸에 선수의 아이디를 입력합니다.')
    st.markdown('###### --> 선수의 공/수 효율 점수와 연봉에 관한 정보가 출력됩니다.')

    st.markdown('### 활용도 / 의미')
    st.markdown('###### -1번 정보를 통해 최근 폼이 좋은 선수를 확인하고 중점적으로 막기 위해 대비합니다. 3번 검색창으로 검색하여 선수가 선호하는 슛 스팟, 선수의 정보를 파악하여 체께적으로 전술을 세웁니다.')
    st.markdown('###### -2번 정보를 통해 부상당한 선수를 제외한 로스터를 확인하여 맞춤형 전술을 공략하는데 참고하면 좋습니다.')
    st.markdown('###### -3번 정보를 통해 특정 궁금한 선수들을 검색하여 선수가 선호하는 슛 스팟, 성공률이 좋은 스팟, 공격 방식을 파악하여 맞춤형으로 수비합니다.')
    st.markdown('###### -4번 정보를 통해 클러치 상황에서 상대팀의 특정 선수들을 검색하여 누가 가장 성공률이 좋은지 파악하여 가장 성공률이 높은 선수를 중점적으로 수비합니다.')
    st.markdown('###### --> 더 나아가 특정 경기 종료 직전 각 팀의 에이스 선수들을 검색하여 승부 예측도 해볼 수 있습니다.')
    st.markdown('###### -5번 정보는 계속 최신화 되는 정보를 통해 선수들의 능력치를 파악합니다.')
    st.markdown('###### -6번 정보를 통해 포지션 별 경기에 영향을 미치는 정도를 파악합니다.')
    st.markdown('###### --> 선수영입, 트레이드 간 한정적인 비용에서 공/수에서 가장 영향력이 좋은 (즉, 경기대비 가성비가 가장 좋은)포지션을 파악하여 선수영입할때 참고') 
    st.markdown('###### -7,8번 데이터를 통하여 현시즌 스텟이 좋은 선수들의 순위와 연봉을 파악합니다.')
    st.markdown('###### --> 능력치 대비 연봉이 과소평과 된 선수들을 파악하여 좋은 가격에 트레이드, 영입하는데 사용합니다.')
    st.markdown('###### -9번 정보를 통해 선수들의 효율성과 연봉을 파악할 수 있습니다.')
    st.markdown('###### --> 제한적인 가격내에서 선수를 영입할 때, 검색하여 각 선수의 정보를 통해 가격대비 능력치가 가장 좋은 선수를 영입하는데 사용')
                
    st.markdown('### 데이터 수집 페이지')
    st.markdown('###### -CBSSPORTS , https://www.cbssports.com/nba/scoreboard/')
    st.markdown('###### -CBSSPORTS , https://www.cbssports.com/nba/injuries/')
    st.markdown('###### -HOOPSHYPE , https://hoopshype.com/salaries/players/')
    st.markdown('###### -ESPN , https://www.espn.com/nba/stats/player')
    st.markdown('###### nba_api 데이터 일부 사용')

    st.markdown('### 데이터 분석 과정')
    st.markdown('###### 선수들의 스텟, 연봉 그리고 핫플레이어, 부상자, 클러치타임정보, 슛스팟정보등을 수집하였습니다.')
    st.markdown('###### 각 정보들을 데이터프레임 형태로 만든 후 어떠한 데이터를 가진지 분석하여 새로운 컬럼도 생성하였습니다.')
    st.markdown('###### 포지션이라는 그룹으로 묶어 새로운 데이터를 표현하는 분석도 해보았습니다.')
    st.markdown('###### 각 데이터 프레임이 가지는 공통된 "ID"라는 컬럼을 통하여 각 데이터에서 "ID"값을 통해 여러정보를 사용하였습니다.')
    st.markdown('###### 스포츠 종목의 경우 아무래도 정보를 그래프로 시각화 하는것이 가시적으로 확인하기 편리하므로 시각화하기 위해 노력했습니다.')

explanation()