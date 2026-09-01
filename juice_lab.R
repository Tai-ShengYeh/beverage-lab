# 飲料設計師實驗室 — R 版（果汁配方最佳化，網格搜尋法）
# 資料來源：Navarrete-González et al. (2026) Sustainable Food Technol., 4, 947-960 (CC-BY 4.0)
# 執行環境：Posit Cloud 或本機 R（不需額外套件）

# ---------- 論文式 9：總多酚 (mg GAE/mL) ----------
tp <- function(a, g, c) {
  224.62*a + 606.16*g + 600.54*c +
  33.90*a*g + 197.52*g*c - 241.47*c*a
}

# ---------- Table 6：黏度 (cP，百分比尺度) ----------
visc <- function(a, g, c) {
  A <- a*100; G <- g*100; C <- c*100
  0.1685*A + 0.0059*G + 0.2709*C + 0.0093*A*G - 0.0044*A*C + 0.0026*G*C
}

# ---------- 式 6 + Table S3：密度 (g/mL) ----------
dens <- function(a, g, c) 1 / (a/1.024 + g/1.053 + c/1.024)

# ========== 把所有可能比例（間隔 1%）全部算一遍 ==========
grid <- expand.grid(a = seq(0, 1, 0.01), g = seq(0, 1, 0.01))
grid$c <- 1 - grid$a - grid$g          # 質量守恆：三者加總 = 1
grid <- grid[grid$c >= -1e-9, ]
grid$TP   <- with(grid, tp(a, g, c))
grid$visc <- with(grid, visc(a, g, c))
grid$dens <- with(grid, dens(a, g, c))

# ---------- 無限制最佳解 ----------
best <- grid[which.max(grid$TP), ]
cat("── 無限制最佳解 ──\n")
cat(sprintf("蘋果 %.0f%%、葡萄 %.0f%%、蔓越莓 %.0f%% → TP = %.1f（黏度 %.1f cP、密度 %.3f）\n\n",
    best$a*100, best$g*100, best$c*100, best$TP, best$visc, best$dens))

# ---------- 有限制最佳解（真實的食品設計） ----------
ok <- subset(grid, visc > 20 & visc < 26 & dens > 1.00 & dens < 1.04)
best2 <- ok[which.max(ok$TP), ]
cat("── 有限制最佳解 ──\n")
cat(sprintf("蘋果 %.0f%%、葡萄 %.0f%%、蔓越莓 %.0f%% → TP = %.1f（黏度 %.1f cP、密度 %.3f）\n",
    best2$a*100, best2$g*100, best2$c*100, best2$TP, best2$visc, best2$dens))
cat("→ 論文的理論最佳解是 14% / 44% / 42% → TP = 564.5，比較看看！\n")

# 進階挑戰：安裝 Bioconductor 的 NutrienTrackeR 套件，分析真實食物的營養成分
