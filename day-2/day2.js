const fs = require('fs');

function countSafeReportsWithDampener(filePath) {
    function isSafeReport(levels) {
        let isIncreasing = null;

        for (let i = 1; i < levels.length; i++) {
            const diff = levels[i] - levels[i - 1];
            if (Math.abs(diff) < 1 || Math.abs(diff) > 3) return false;
            if (isIncreasing === null) {
                isIncreasing = diff > 0;
            } else {
                if ((isIncreasing && diff < 0) || (!isIncreasing && diff > 0)) return false;
            }
        }
        return true;    }

    function isSafeWithDampener(levels) {
        for (let i = 0; i < levels.length; i++) {
            const modifiedLevels = levels.slice(0, i).concat(levels.slice(i + 1));
            if (isSafeReport(modifiedLevels)) {
                return true;
            }
        }
        return false;
    }

    const data = fs.readFileSync(filePath, 'utf8');
    const reports = data.trim().split('\n');

    let safeCount = 0;

    reports.forEach(report => {
        const levels = report.split(" ").map(Number);

        if (isSafeReport(levels) || isSafeWithDampener(levels)) {
            safeCount++;
        }
    });
    return safeCount;
}

const filePath = 'input2.txt'; 
console.log(`Number of safe reports: ${countSafeReportsWithDampener(filePath)}`);
