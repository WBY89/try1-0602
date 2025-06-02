import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import os  # 新增路径处理库

# 页面配置
st.set_page_config(
    page_title="Chloe WANG个人校招求职简历",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 全局样式
def global_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;700&display=swap');
    body { font-family: 'Noto Sans SC', sans-serif; color: #333; }
    .header { font-size: 2.5rem; font-weight: 700; color: #2B6CB0; }
    .subheader { font-size: 1.2rem; color: #6B7280; margin-bottom: 1rem; }
    .section-title { color: #2B6CB0; border-bottom: 2px solid #2B6CB0; padding-bottom: 0.5rem; margin: 2rem 0; }
    .achievement { color: #155E75; font-weight: bold; }
    .skill-item { background-color: #F3F4F6; padding: 0.2rem 0.6rem; border-radius: 12px; margin-right: 0.5rem; margin-bottom: 0.5rem; }
    .contact-info { text-align: right; }
    .footer { border-top: 1px solid #E5E7EB; padding: 1rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 图片路径统一管理函数
def get_image_path(image_name):
    """生成标准化图片路径，支持本地和线上环境"""
    # 定义资源目录（建议在项目根目录创建static/images文件夹）
    base_dir = os.path.dirname(os.path.abspath(__file__))  # 获取当前文件路径
    return os.path.join(base_dir, "static", "images", image_name)

# 主页内容
def home_page():
    global_style()
    col1, col2 = st.columns([3, 1], gap="large")
    
    # 左侧个人信息
    with col1:
        st.markdown("<div class='header'>王冰颖 (Chloe Wang)</div>", unsafe_allow_html=True)
        st.markdown("<div class='subheader'>对外经济贸易大学本科+香港中文大学硕士 | 4市场营销与管理咨询领域实习经历 | 数据驱动型决策者</div>", unsafe_allow_html=True)
        st.markdown("""
        拥有美妆、3C跨行业营销策划、数据运营与咨询4段实习经验，擅长通过消费者洞察与数字化手段驱动业务增长。<br>
        熟练运用 SQL、SPSS 等数据分析工具，在小红书平台运营、品牌全案策划、ESG 咨询领域有突出成果。<br>
        工作上的效率至上J人，生活中的自由探索P人。
        """, unsafe_allow_html=True) # 添加 unsafe_allow_html=True 以解析 <br>
    
    # 右侧联系方式（带图片校验）
    with col2:
        image_path = get_image_path("resumepicture1.jpg")
        if os.path.exists(image_path):
            st.image(image_path, width=150)
        else:
            st.warning("简历照片未找到", icon="⚠️")
        add_vertical_space(1) # 在照片和联系信息之间添加一些垂直空间
        st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>手机：</strong> (+86) 18515590199</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>邮箱：</strong> 18515590199@163.com</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>微信：</strong> wby7196</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    add_vertical_space(2)

# 教育背景页面（统一修改图片路径）
def education_page():
    st.markdown("<h2 class='section-title'>教育背景</h2>", unsafe_allow_html=True)
    # 硕士
    st.markdown("<h3>香港中文大学 <span class='subheader'>硕士</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 商学院 市场营销（2024.08-2025.11，香港）")
    st.markdown("- 核心课程：营销管理、消费者行为、机器学习与数字营销")
    add_vertical_space(1)
    # 本科
    st.markdown("<h3>对外经济贸易大学 <span class='subheader'>本科</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown(f"- 德语（企业管理）辅修国际经济与贸易（2020.09-2024.06，北京）<br>GPA：3.67/4.0（<span class='achievement'>年级前10%</span>）", unsafe_allow_html=True)
    st.markdown("- 核心课程：德语视听说、财务会计、公司理财、国际金融学、管理科学、全球营销")
    add_vertical_space(2)
    # 奖项
    st.markdown("<h3 class='section-title'>所获奖项</h3>", unsafe_allow_html=True)
    st.markdown("- 校级综合二等奖学金")
    st.markdown("- 院级优秀学生")
    st.markdown("- 2022年国家级大学生创新创业比赛（创业实践类）<span class='achievement'>国家级一等奖</span>", unsafe_allow_html=True)
    st.markdown("- 挑战杯国奖")

# 实习经历页面（统一修改图片路径）
def experience_page():
    st.markdown("<h2 class='section-title'>实习经历</h2>", unsafe_allow_html=True)
    # 小红书实习
    st.markdown("<h3>小红书-书行科技（北京）有限公司 <span class='subheader'>商业部</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2024.01-2024.05，北京", unsafe_allow_html=True)
    st.markdown("""
    - 营销策划：参与品牌大单品全案，人群资产从105万提升至1238万，核心人群渗透率从6%提升至19%，贡献当月27%成交量  
    - 广告投放：协助策划一汽大众、沃尔沃广告方案，月均获取1100+优质线索  
    - 数据监控：运营数据看板，优化人群/买词/素材，梳理行业SOP  
    - 产品基建：补充3000+SPU信息，推动600+SPU迭代，数据库准确率达到90%
    """)
    add_vertical_space(1)
    # 宝马实习
    st.markdown("<h3>宝马（中国）汽车贸易有限公司 <span class='subheader'>市场部</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2023.10-2023.12，北京", unsafe_allow_html=True)
    st.markdown("""
    - 竞品分析：分析4个竞品，输出3份报告支持广州车展  
    - 内容营销：规划KOL投放矩阵，筛选300+KOL，发布20条内容，CPE降低20%；公众号阅读量增长15%  
    - 活动策划：策划2场车友会，参与人数提升40%
    """)
    add_vertical_space(1)
    # 普华永道实习
    st.markdown("<h3>普华永道 <span class='subheader'>OFS</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2023.06-2023.08，北京", unsafe_allow_html=True)
    st.markdown("""
    - 行业研究：撰写垃圾焚烧发电行业报告，编制3篇ESG报告  
    - 数据调研：参与企业ESG数据鉴证，组织10+专家访谈
    """)
    add_vertical_space(1)
    # 玛氏箭牌实习
    st.markdown("<h3>玛氏箭牌 <span class='subheader'>Bekind市场部</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2022.07-2022.12，北京", unsafe_allow_html=True)
    st.markdown("""
    - blogger对接：合作200+头腰部博主，双11直播GMV增长近10倍  
    - 数据分析：周度监测数据，负评率降低20%
    """)

# 项目经历页面（统一修改图片路径）
def project_page():
    st.markdown("<h2 class='section-title'>项目与社团经历</h2>", unsafe_allow_html=True)
    # 创新创业项目
    st.markdown("<h3>“Puppy Hotel”啪噼客栈 <span class='subheader'>项目负责人</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2022.03-2023.02 | 成果：国家级大学生创新创业大赛国奖")
    st.markdown("""
    - 市场调研：评估竞争对手，访谈80+用户，确定差异化卖点  
    - 产品推广：多渠道拉新，与KOKOWAN品牌置换资源合作，1个月获取3000+种子用户
    """)
    add_vertical_space(1)
    # 社团经历
    st.markdown("<h3>对外经济贸易大学创新创业中心 <span class='subheader'>部长</span></h3>", unsafe_allow_html=True)
    # 已移除图片相关代码
    st.markdown("- 2020.09-2021.10")
    st.markdown("""
    - 团队管理：带领10人团队，秋季招新人数增长40%  
    - 商务对接：引入10+家外联商家，半年度获取总计8万元外联资金
    """)

# 技能与证书页面
def skill_page():
    st.markdown("<h2 class='section-title'>技能与证书</h2>", unsafe_allow_html=True)
    
    # 语言能力
    st.markdown("语言技能：")
    st.markdown(f"- 英语：雅思7.0（L:7 R:7 S:7 W:7），GRE 323+4")
    st.markdown(f"- 德语：德语专四优秀（90分），德福18（C1等级，德语听说读写流利）")
    
    add_vertical_space(1)
    
    # 专业技能
    st.markdown("专业工具与能力：")
    skills = [ "SPSS", "SQL", "消费者行为分析", "数字营销", "ESG咨询"]
    for skill in skills:
        st.markdown(f"<span class='skill-item'>{skill}</span>", unsafe_allow_html=True)
    
    add_vertical_space(1)
    
    # 兴趣爱好
    st.markdown("兴趣爱好：")
    hobbies = ["游泳", "羽毛球", "竖笛",  "象棋"]
    for hobby in hobbies:
        st.markdown(f"<span class='skill-item'>{hobby}</span>", unsafe_allow_html=True)

# 多页面导航
def main():
    st.sidebar.markdown("# 王冰颖个人简历", unsafe_allow_html=True)
    page = st.sidebar.radio("导航", ["主页", "教育背景", "实习经历", "项目经历", "技能与证书"])
    
    if page == "主页":
        home_page()
    elif page == "教育背景":
        education_page()
    elif page == "实习经历":
        experience_page()
    elif page == "项目经历":
        project_page()
    else:
        skill_page()
    
    # 页脚
    st.markdown("<div class='footer'>Created by ❤️ Chloe WANG  | 2025</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()