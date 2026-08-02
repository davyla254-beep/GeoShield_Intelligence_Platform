

c1,c2,c3,c4 = st.columns(4)

c1.metric(
"Counties",
len(df)
)

c2.metric(
"Average NDVI",
round(df["NDVI"].mean(),3)
)

c3.metric(
"Average Rainfall",
round(df["Rainfall_mm"].mean(),1)
)

highest=df.loc[df["Drought_Risk"].idxmax()]

c4.metric(
"Highest Risk",
highest["County"]
)
