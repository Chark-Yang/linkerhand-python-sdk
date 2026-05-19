cat > ~/linkerhand-python-sdk/example/linker_hand_mujoco/run_linker_hand.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

# 让 shell 能使用 conda activate
source ~/miniconda3/etc/profile.d/conda.sh
conda activate l20

# 自动拿到 PyQt5 的 Qt 根目录，避免写死 python3.9 路径
PYQT_QT_BASE="$(python - <<'PY'
import os
from PyQt5.QtCore import QLibraryInfo
p = QLibraryInfo.location(QLibraryInfo.PluginsPath)  # .../PyQt5/Qt5/plugins
print(os.path.dirname(p))                             # .../PyQt5/Qt5
PY
)"

export QT_PLUGIN_PATH="$PYQT_QT_BASE/plugins"
export QT_QPA_PLATFORM_PLUGIN_PATH="$PYQT_QT_BASE/plugins/platforms"
export LD_LIBRARY_PATH="$PYQT_QT_BASE/lib:${LD_LIBRARY_PATH:-}"
export QT_QPA_PLATFORM=xcb

exec python ~/linkerhand-python-sdk/example/linker_hand_mujoco/linker_hand.py
EOF