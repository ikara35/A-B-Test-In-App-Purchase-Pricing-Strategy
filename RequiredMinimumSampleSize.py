from statsmodels.stats.power import TTestIndPower

# Parameters for power analysis
alpha = 0.1       # Type I error rate (significance level)
power = 0.8       # Statistical power (probability of detecting a true effect)
std_dev = 1.5     # Standard deviation of the metric (e.g., revenue per user)
effect_diff = 0.88 - 0.80 # Expected difference in means (e.g., ARPU difference between groups)

# Calculate the effect size (Cohen's d)
# Cohen's d quantifies the standardized difference between two means.
# It's calculated as the difference between the means divided by the standard deviation.
effect_size = effect_diff / std_dev

# Perform sample size calculation
# TTestIndPower is used for power analysis of a two-sample independent t-test.
analysis = TTestIndPower()

# Solve for the required sample size per group
# 'alternative='two-sided'' specifies that we are looking for a difference in either direction (increase or decrease).
sample_size = analysis.solve_power(effect_size=effect_size,
                                   power=power,
                                   alpha=alpha,
                                   alternative='two-sided')

# Print the calculated minimum sample size, rounded down to the nearest integer
print(f"Required minimum sample size per group ≈ {int(sample_size)} users")