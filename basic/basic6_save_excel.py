import openpyxl

# 1) 엑셀 만들기
workbook = openpyxl.Workbook()

# 2) 엑셀 워크시트 만들기
sheet = workbook.create_sheet('참가자')
#TODO

# 3) 데이터 추가하기
sheet['A1'] = '참가번호'
sheet['B1'] = '성명'

sheet['A2'] = 1
sheet['B2'] = '오일남'

# 4) 엑셀 저장
workbook.save('/Users/naegwonhwang/Documents/오징어게임.xlsx')



