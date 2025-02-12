library(data.table)
library(limma)
library(DMRcate)
######################################################## Data and metadata loading and normalization
# GSE179325 data: whole blood 473 positive and 101 negative SARS-CoV-2 individuals #Illumina Infinium MethylationEPIC Beadchip data
GSE179325<-as.data.frame(fread("path",header=T))
rownames(GSE179325) <- GSE179325$ID
# Convert beta values to M-values (for better statistical properties)
beta_values <- GSE179325[, -1]  # Exclude ID column
m_values <- log2(beta_values / (1 - beta_values))
# metadata 
metaGSE179325_list <- readLines("path/GSE179325_series_matrix.txt")
# Severity inf: element 42 in list
metadata_string <- metaGSE179325_list[[42]]
metadata_split <- strsplit(metadata_string, "\t")[[1]]
disease_states <- metadata_split[-1]
disease_states <- gsub("disease state: ", "", disease_states)
disease_states <- trimws(disease_states)
sample_info<-cbind(colnames(GSE179325[, -1]),disease_states)
colnames(sample_info)<- ("Sample_Name","Group")

######################################################## Checking beta values and M values distribution
png("beta_values_325.png", width = 600, height = 600, bg = "white")  
library(RColorBrewer)
beta_values <- as.matrix(GSE179325[, -1])
unique_groups <- unique(sample_info$Group)
num_groups <- length(unique_groups)
colors <- brewer.pal(max(3, num_groups), "Dark2") 
# densities for each group manually
par(mfrow = c(1, 1))
plot(NULL, xlim = range(beta_values, na.rm = TRUE), ylim = c(0, 6), 
     main = "Beta-Values Distribution", xlab = "Beta-Value", ylab = "Density")
for (i in seq_along(unique_groups)) { group <- unique_groups[i]
  group_beta_values <- beta_values[, sample_info$Group == group]  
  density_curve <- density(as.vector(group_beta_values), na.rm = TRUE)  
  lines(density_curve, col = colors[i], lwd = 2) }
legend("topright", legend = unique_groups, col = colors[1:num_groups], 
       lwd = 2, box.lwd = 0, cex = 0.8)
grid()
dev.off()
png("m_values_325.png", width = 600, height = 600, bg = "white") 
library(RColorBrewer)
beta_values <- as.matrix(GSE179325[, -1])
m_values <- log2(beta_values / (1 - beta_values))
unique_groups <- unique(sample_info$Group)
num_groups <- length(unique_groups)
colors <- brewer.pal(max(3, num_groups), "Dark2")  
# densities for each group manually
par(mfrow = c(1, 1))
plot(NULL, xlim = range(m_values, na.rm = TRUE), ylim = c(0, 0.2), 
     main = "M-Values Distribution", xlab = "M-Value", ylab = "Density")
for (i in seq_along(unique_groups)) { group <- unique_groups[i]
  group_m_values <- m_values[, sample_info$Group == group]  
  density_curve <- density(as.vector(group_m_values), na.rm = TRUE)  
  lines(density_curve, col = colors[i], lwd = 2) }
legend("topright", legend = unique_groups, col = colors[1:num_groups], 
       lwd = 2, box.lwd = 0, cex = 0.8)
grid()
dev.off()

######################################################## Design Matrix and Contrasts
# Clean the disease states to remove extra quotes
disease_states_clean <- gsub('^"|"$', '', disease_states)
disease_states_factor <- factor(disease_states_clean, levels = c("NEGATIVE", "MILD", "SEVERE"))
design <- model.matrix(~ 0 + disease_states_factor)
colnames(design) <- levels(disease_states_factor)
# contrasts
contrast_matrix <- makeContrasts(
    SEVEREvsNEGATIVE = SEVERE - NEGATIVE,
    SEVEREvsMILD = SEVERE - MILD,
    levels = design)
contrast_matrix

#
contrasts
