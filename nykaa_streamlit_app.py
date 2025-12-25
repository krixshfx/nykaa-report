import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

# --- Data Loading ---
@st.cache_data
def load_data():
    df = pd.read_csv('nykaa_market_report/data/report_data.csv')
    return df

df = load_data()

# --- Sidebar Navigation ---
st.sidebar.title("Nykaa Market Research")
section = st.sidebar.radio(
    "Go to",
    (
        "Executive Summary",
        "Market Context",
        "SWOT Analysis",
        "PESTEL Analysis",
        "Competitive Positioning",
        "Strategic Recommendations",
        "View Data"
    )
)

# --- Main Content ---

if section == "Executive Summary":
    st.title("Nykaa Market Research Report")
    st.header("1. Executive Dashboard")

    # KPIs
    col1, col2, col3 = st.columns(3)
    revenue_fy24 = df[df['Metric'] == 'Revenue FY24 (INR)']['Value'].values[0]
    net_profit_fy24 = df[df['Metric'] == 'Net Profit FY24 (INR)']['Value'].values[0]
    market_share = df[df['Metric'] == 'Online BPC Market Share 2023']['Value'].values[0]

    col1.metric("Revenue (FY24)", f"₹{revenue_fy24}")
    col2.metric("Net Profit (FY24)", f"₹{net_profit_fy24}")
    col3.metric("Online BPC Market Share", f"{market_share}")

    st.markdown("---")

    # Charts
    col1, col2 = st.columns(2)
    with col1:
        st.image('nykaa_market_report/visualizations/financial_performance.png', caption="Nykaa's Financial Performance")
    with col2:
        st.image('nykaa_market_report/visualizations/revenue_mix.png', caption="Nykaa's Revenue Mix")

elif section == "Market Context":
    st.header("2. Market Context & Nykaa’s Role")
    st.markdown("""
    The Indian Beauty & Personal Care (BPC) market is a high-growth sector, valued at **~$23.4B in 2024** and projected to reach **~$33.8B by 2033** (CAGR: ~4.2%). Nykaa has been a primary driver and beneficiary of this growth, establishing itself as the leading online BPC retailer with a **~28% market share**.

    Nykaa's success is built on an **inventory-led, omnichannel model** that guarantees product authenticity and a curated customer experience. This has fostered significant brand trust and a loyal customer base, evidenced by a high repeat customer rate. However, the market is undergoing a significant shift.
    """)
    st.image('nykaa_market_report/visualizations/market_growth.png', caption='Indian BPC Market Growth')

elif section == "SWOT Analysis":
    st.header("3. Prioritized SWOT Analysis")
    st.subheader("Materiality Scorecard")
    st.image('nykaa_market_report/visualizations/swot_materiality.png', caption='SWOT Materiality Scorecard')
    st.subheader("Most Critical Factor: Intense Competition")
    st.markdown("""
    *   **Quantitative Signal:** The entry of Reliance's Tira, Tata Cliq Palette, and expanded offerings from Myntra and Amazon are fragmenting the market. While Nykaa holds ~28% share, new players are quickly gaining traction.
    *   **Business Implication:** Increased pressure on pricing, customer acquisition costs, and innovation. Nykaa's "moat" is shrinking.
    *   **Confidence Level:** High. The new entrants are well-capitalized and have a strong retail footprint.
    *   **Assumption:** Competitors will continue to invest aggressively to gain market share.
    """)

elif section == "PESTEL Analysis":
    st.header("4. Prioritized PESTEL Analysis")
    st.subheader("Most Critical Factor: Social & Technological Convergence")
    st.markdown("""
    *   **Quantitative Signal:** India has over 900 million internet users, and digital adoption in Tier II/III cities is rapidly increasing. Social commerce and influencer marketing are driving BPC trends.
    *   **Business Implication:** Nykaa's future growth is contingent on its ability to leverage technology (AI/AR) and social trends to personalize the customer experience at scale. The "one-size-fits-all" e-commerce model is obsolete.
    *   **Confidence Level:** Very High. All data points to the increasing fusion of social media, content, and commerce.
    *   **Assumption:** The demand for personalized, digitally-native experiences will continue to accelerate.
    """)

elif section == "Competitive Positioning":
    st.header("5. Competitive Positioning")
    st.subheader("Positioning Map")
    st.image('nykaa_market_report/visualizations/market_share.png', caption="Online BPC Market Share 2023")
    st.markdown("""
    **Interpretation:** Nykaa holds a strong position in the "premium, curated" space. However, its most vulnerable flank is to competitors who can offer a "good enough" curated experience at a lower price point, or a much wider assortment with faster delivery.
    """)
    st.subheader("Competitive Scorecard")
    st.markdown("""
| Competitor | Price | Assortment | Trust | Reach | Vulnerable Point |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nykaa** | Premium | Curated | High | High | **Price & Speed** |
| **Myntra** | Mid | Broad | Med | High | BPC is not core focus |
| **Amazon** | Low | Very Broad | Med | Very High | Lacks curation/trust |
| **Tira** | Mid-Premium| Curated | Low-Med | Growing | New, unproven |
    """)

elif section == "Strategic Recommendations":
    st.header("6. Strategic Implications & Recommendations")
    st.subheader("1. Deepen the Moat with Private Labels & Services")
    st.markdown("""
    *   **Rationale:** Private labels offer higher margins and a unique product offering that cannot be replicated by competitors. Services (e.g., virtual consultations, personalized beauty plans) can create stickier customer relationships.
    *   **Quantitative Signal:** Nykaa's private label brands have a 112% CAGR in the fashion segment, demonstrating potential.
    *   **Trade-off:** Requires significant investment in R&D and marketing for the private label brands.
    """)
    st.subheader("2. Targeted Expansion into Tier II/III Cities")
    st.markdown("""
    *   **Rationale:** These markets are the next frontier of growth, but require a different strategy (e.g., smaller store formats, different product assortment, vernacular content).
    *   **Quantitative Signal:** Rising disposable incomes and internet penetration in these cities.
    *   **Trade-off:** Higher logistical complexity and potentially lower average order values.
    """)
    st.subheader("3. Optimize the Omnichannel Experience for Convenience")
    st.markdown("""
    *   **Rationale:** Leverage the physical store network for "click-and-collect," express delivery, and hyperlocal marketing. This can be a key differentiator against online-only players.
    *   **Quantitative Signal:** Over 150 existing physical stores provide a strong foundation.
    *   **Trade-off:** Requires investment in store technology and inventory management systems.
    """)

elif section == "View Data":
    st.header("Raw Data")
    st.dataframe(df)
