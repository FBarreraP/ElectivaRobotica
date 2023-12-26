import numpy

nums1 = numpy.array([3,7,4,9,1])
nums2 = numpy.array([[6.3,7.2,1.1],[9.6,5.7,2.4]])
print("Datos y tamaño del vector nums1: %s y %d" %(nums1[0:4],nums1.size))
print("Datos y tamaño del vector nums2: %s y %d(%d)" %(nums2,len(nums2),nums2.size)) 

nums1[2] = 100
nums2[0,:] = 83
print("Datos y tamaño del vector nums1: %s y %d" %(nums1[1:4],nums1.size))
print("Datos y tamaño del vector nums2: %s y %d(%d)" %(nums2,len(nums2),nums2.size)) 