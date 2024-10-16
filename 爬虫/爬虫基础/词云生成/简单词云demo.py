from wordcloud import wordcloud
import matplotlib.pyplot as plt

text = "创新、科技、人工智能、数据、分析、未来、智能、云计算、物联网、区块链、机器学习、自动化、网络安全、移动应用、用户体验、社交媒体、电子商务、环保、可持续发展、健康、医疗、生物科技、能源、金融、创业、投资、教育、文化、旅游、娱乐、艺术、设计、时尚、美食、体育、音乐、电影、游戏、旅游、探索、发现、自由、梦想、希望、勇气、坚持、友谊、爱情、家庭、幸福、和平、尊重、包容、平等、合作、共赢、责任、信任、感恩、成长、智慧、自由、开放、多元、共享、创新、激情、卓越、领导、管理、团队、战略、营销、品牌、服务、质量、用户、产品、设计、研发、技术、创新、创业、投资、金融、经济、市场、竞争、合作、发展、未来、全球化、国际化、本土化、趋势、时尚、文化、艺术、历史、传统、现代、科学、哲学、教育、学习、成长、心理、健康、医疗、科技、环境、社会、公益、责任、道德、伦理、政治、法律、自由、民主、平等、尊重、包容、多元、和平、安全、稳定、繁荣、发展、机遇、挑战、创新、突破、变革、转型、升级、优化、提升、拓展、延伸、深化、加强、巩固、拓展、创新、拓展、升级、转型、变革、发展、共赢、协同、合作、共享、开放、包容、多元、自由、平等、民主、法治、公正、廉洁、诚信、友善、和谐、美丽、安全、稳定、繁荣、幸福、健康、快乐、自由、梦想、希望、勇气、坚持、奋斗、拼搏、进取、努力、付出、收获、成就、尊重、感恩、奉献、爱心、责任、公益、环保、可持续、未来、探索、发现、智慧、领导力、创新思维、团队协作、战略眼光、市场营销、品牌影响力、优质服务、产品质量、用户体验、研发实力、技术创新、创业精神、投资眼光、经济发展、市场竞争、合作共赢、全球化视野、本土化运营、国际化战略、时尚潮流、文化传承、艺术创新、历史积淀、现代科技、科学探索、哲学思考、教育培训、学习成长、心理健康、医疗服务、科技创新、环境保护、社会责任、道德规范、政治稳定、法律保障、民主自由、平等公正、法治精神、社会和谐、美丽中国、安全稳定、繁荣发展、机遇挑战、创新突破、变革转型、升级优化、提升拓展、深化加强、巩固发展、共赢协同、共享开放、包容多元、自由平等、民主法治、公正廉洁、诚信友善、和谐美丽、安全稳定、幸福繁荣、健康快乐、梦想希望、勇气坚持、奋斗拼搏、进取努力、付出收获、成就尊重、感恩奉献、爱心责任。"

wc = wordcloud.WordCloud(
    font_path='../../../font/MSYH.TTC',
    background_color='white',
    max_font_size=30,
    min_font_size=10
)

wc.generate(text)
wc.to_file('image.png')
plt.imshow(wc) # 创建图像
plt.axis('off') #关闭坐标轴
plt.show()