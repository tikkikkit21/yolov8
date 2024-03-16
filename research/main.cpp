#include <onnxruntime_cxx_api.h>
void main(){
  //check providers
  auto providers = Ort::GetAvailableProviders();
  for (auto provider : providers) {
    std::cout << provider << std::endl;
  }
}
