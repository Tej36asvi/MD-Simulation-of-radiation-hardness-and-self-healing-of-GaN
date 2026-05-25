import pandas as pd
import matplotlib.pyplot as plt
import io

# Your dataset
data = """Frame WignerSeitz.interstitial_count WignerSeitz.vacancy_count
0 0 0 
1 1 1 
2 3 3 
3 6 6 
4 13 13 
5 22 22 
6 36 36 
7 59 59 
8 86 86 
9 111 111 
10 160 160 
11 180 180 
12 220 220 
13 253 253 
14 301 301 
15 344 344 
16 369 369 
17 411 411 
18 424 424 
19 445 445 
20 461 461 
21 465 465 
22 486 486 
23 484 484 
24 494 494 
25 474 474 
26 466 466 
27 472 472 
28 463 463 
29 478 478 
30 444 444 
31 458 458 
32 444 444 
33 449 449 
34 431 431 
35 442 442 
36 417 417 
37 398 398 
38 378 378 
39 356 356 
40 356 356 
41 359 359 
42 338 338 
43 318 318 
44 289 289 
45 296 296 
46 289 289 
47 299 299 
48 287 287 
49 279 279 
50 283 283 
51 257 257 
52 231 231 
53 224 224 
54 217 217 
55 197 197 
56 173 173 
57 168 168 
58 153 153 
59 148 148 
60 134 134 
61 153 153 
62 153 153 
63 184 184 
64 160 160 
65 148 148 
66 158 158 
67 153 153 
68 127 127 
69 122 122 
70 114 114 
71 104 104 
72 105 105 
73 98 98 
74 96 96 
75 103 103 
76 102 102 
77 107 107 
78 100 100 
79 109 109 
80 108 108 
81 122 122 
82 136 136 
83 107 107 
84 107 107 
85 100 100 
86 94 94 
87 99 99 
88 95 95 
89 99 99 
90 105 105 
91 110 110 
92 107 107 
93 102 102 
94 102 102 
95 110 110 
96 103 103 
97 100 100 
98 102 102 
99 106 106 
100 99 99 
101 86 86 
102 92 92 
103 86 86 
104 98 98 
105 96 96 
106 104 104 
107 89 89 
108 79 79 
109 99 99 
110 107 107 
111 98 98 
112 111 111 
113 108 108 
114 105 105 
115 105 105 
116 101 101 
117 98 98 
118 100 100 
119 101 101 
120 109 109 
121 114 114 
122 110 110 
123 106 106 
124 112 112 
125 112 112 
126 107 107 
127 109 109 
128 113 113 
129 118 118 
130 113 113 
131 104 104 
132 114 114 
133 107 107 
134 106 106 
135 98 98 
136 110 110 
137 102 102 
138 111 111 
139 104 104 
140 113 113 
141 113 113"""

# Load the data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(data), sep=r'\s+')

# Create the plot
plt.figure(figsize=(10, 6))

# Plot Interstitials (Solid Blue Line)
plt.plot(df['Frame'], df['WignerSeitz.interstitial_count'], 
         label='Interstitials', color='blue', linewidth=3, alpha=0.7)

# Plot Vacancies (Dashed Red Line - placed on top so both are visible)
plt.plot(df['Frame'], df['WignerSeitz.vacancy_count'], 
         label='Vacancies', color='red', linestyle='--', linewidth=2)

# Labeling and formatting
plt.title('Point Defect Evolution (Wigner-Seitz Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Frame', fontsize=12)
plt.ylabel('Defect Count', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()