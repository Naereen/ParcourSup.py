# Copyright (C) 2018 José Paumard
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

@Internat
Feature: Gestion des internats section 5.1
  Algorithme quotidien Internat étant donné la position d'admission B

  Les tests sont répartis en sections, dans des scénarios qui regroupent des formations
  partageant les mêmes caractéristiques :
  - le rang limite de proposition est-il plus grand ou plus petit que la capacité
    d'accueil de la formation ?
  - l'internat a-t-il une capacité d'accueil plus grande ou plus petite que le nombre
    de candidat-e-s ?
  - la valeur de B est-elle plus petite ou égale au nombre de candidat-e-s ?
  - la valeur de B est-elle plus grande ou plus petite que la capacité d'accueil de l'internat.

  Par nature, B ne doit pas être plus grand que le nombre de candidat-e-s avec internat

  @1.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 10 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6 | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C6 | C1 C6 C2 C3   | C4 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C6 | C1 C6 C2 C3   | C4 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6 | C1 C2 C3 C4   | C5         |

  @1.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 5 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @2.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 10 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6 | C1 C2 C3 C4   | C5 C6      |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C6 | C1 C6 C2 C3   | C4 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6 | C1 C2 C3 C4   | C5         |

  @2.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 5 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat  | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | -          |

  @3.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 10 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation    | prop_internat  | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C6    | C1 C6 C2 C3 C4 | C5         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C6    | C1 C6 C2 C3 C4 | C5         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | -          |

  @3.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 5 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat  | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4    | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4    | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | -          |

  @4.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 10 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation    | prop_internat     | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | -          |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C5 C6 | C1 C6 C2 C3 C4 C5 | -          |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | -          |

  @4.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 5 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat  | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | C6         |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C5 | C1 C2 C3 C4 C5 | -          |

  @5.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @5.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @6.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @6.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 4
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @7.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @7.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |


  @8.1
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |

  @8.2
  Scenario Template: Gestion des internats à capacité d'accueil suffisante
    Given une formation dont le rang limite de proposition est 3 et dont la capacité d'accueil est 4
    And un internat dont la capacité d'accueil est 10
    And la valeur de B est <B>
    And les candidat-e-s à la formation sont <candidats>
    And les candidat-e-s à l'internat sont <cdts_internat>
    And les candidat-e-s à la formation sans internat sont <cdts_sans_internat>
    And le classement à l'internat est <cl_internat>
    When l'ordre d'appel est calculé
    Then les candidat-e-s suivant-e-s reçoivent une proposition pour la formation <prop_formation>
    And les candidat-e-s suivant-e-s reçoivent une proposition pour l'internat <prop_internat>
    And les candidat-e-s suivant-e-s sont en attente pour l'internat <en_attente>
    Examples:
      | B | candidats         | cdts_internat     | cdts_sans_internat | cl_internat       | prop_formation | prop_internat | en_attente |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4    | C1 C2 C3 C4   | C5 C6      |
      | 6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4        | C1 C6 C2 C3 C4 C5 | C1 C2 C3 C4    | C1 C2 C3 C4   | C6 C5      |
      | 5 | C1 C2 C3 C4 C5 C6 | C1 C2 C3 C4 C5    | C1 C2 C3 C4 C6     | C1 C2 C3 C4 C5    | C1 C2 C3 C4    | C1 C2 C3 C4   | C5         |
