from onnxruntime.quantization import quantize_dynamic

ONNX_32 = 'best.onnx'
import sys
if len(sys.argv) == 2:
    ONNX_32 = sys.argv[1]

quantize_dynamic(ONNX_32, 'quantized.onnx')
