import uproot3 as up
import awkward1 as ak
import uproot3_methods
import numpy as np
import matplotlib.pyplot as plt

rootf = "/home/jyshin/tpairstudy/dilep/Events/run_01/test1.root"

dat = up.open(rootf)
tree = dat['LHEF']

#Extract PID, PT, M, Phi, Eta, Status array of Particles from Root File
PID_arr,PT_arr,M_arr,Phi_arr,Eta_arr,Stat_arr,E_arr = tree.arrays(['Particle.PID','Particle.PT','Particle.M','Particle.Phi','Particle.Eta','Particle.Status','Particle.E'],outputtype=tuple)

#Muon & Muon Neutrino Pt, Eta, Phi, Mass
mu_pt = PT_arr[(PID_arr == 13) & (Stat_arr == 1)]
mu_nu_pt = PT_arr[(PID_arr == -14) & (Stat_arr == 1)]

mu_eta = Eta_arr[(PID_arr == 13) & (Stat_arr == 1)]
mu_nu_eta = Eta_arr[(PID_arr == -14) & (Stat_arr == 1)]

mu_phi = Phi_arr[(PID_arr == 13) & (Stat_arr == 1)]
mu_nu_phi = Phi_arr[(PID_arr == -14) & (Stat_arr == 1)]

mu_m = M_arr[(PID_arr == 13) & (Stat_arr == 1)]
mu_nu_m = M_arr[(PID_arr == -14) & (Stat_arr == 1)]

#b-quark pt, Phi in W --> Muon Event
nEvents = int(len(PID_arr))
selEvents = []
for ievt in range(nEvents):
	if 13 not in PID_arr[ievt] : continue
	idx = np.where(PID_arr[ievt] == 13)
	if Stat_arr[ievt][idx] != 1 : continue
	selEvents.append(ievt)
results = np.array(selEvents, dtype=np.dtype('int64'))

b_pt = []
b_phi = []
b_E = []
b_m = []
for i in results:
	b_pt.append(PT_arr[i][np.where(PID_arr[i] == 5)])
	b_phi.append(Phi_arr[i][np.where(PID_arr[i] == 5)])
	b_E.append(E_arr[i][np.where(PID_arr[i] == 5)])
	b_m.append(M_arr[i][np.where(PID_arr[i] == 5)])

# W Transverse Mass
W_mT_s = 2*mu_pt*mu_nu_pt*(1 - np.cos((mu_phi - mu_nu_phi)))
W_mT = np.sqrt(W_mT_s)

plt.hist(W_mT.flatten())
plt.show()
plt.close()

#Muon & Muon Neutrino TLorentzVector
mu_vec = uproot3_methods.TLorentzVectorArray.from_ptetaphim(mu_pt, mu_eta, mu_phi, mu_m)
mu_nu_vec = uproot3_methods.TLorentzVectorArray.from_ptetaphim(mu_nu_pt, mu_nu_eta, mu_nu_phi, mu_nu_m)

# W boson PT & Phi & E

W_vec = mu_vec + mu_nu_vec

w_pt = W_vec.pt
w_phi = W_vec.phi
w_E = W_vec.E

b_m_s = []
for i in range(int(len(b_m))):
	b_m_s.append(pow(b_m[i],2))

top_mt_s = W_mT_s + (b_m_s) + 2*(w_E*b_E - w_pt*b_pt*np.cos(w_phi - b_phi))
top_mt = np.sqrt(top_mt_s)
#top_mt_s = 2 * w_pt *b_pt * (1 - np.cos((w_phi - b_phi)))
#top_mt = np.sqrt(top_mt_s)

plt.hist(top_mt.flatten(),bins=70)
plt.xlim(0,700)
plt.show()
plt.close()
