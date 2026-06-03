---
search:
  boost: 10.0
---

# Class: MedicalHealth 


_Information about health, medical conditions or health care_



<div data-search-exclude markdown="1">



URI: [pd:MedicalHealth](https://w3id.org/lmodel/dpv/pd/MedicalHealth)





```mermaid
 classDiagram
    class MedicalHealth
    click MedicalHealth href "../MedicalHealth/"
      External <|-- MedicalHealth
        click External href "../External/"
      

      MedicalHealth <|-- BloodType
        click BloodType href "../BloodType/"
      MedicalHealth <|-- DNACode
        click DNACode href "../DNACode/"
      MedicalHealth <|-- Disability
        click Disability href "../Disability/"
      MedicalHealth <|-- DrugTestResult
        click DrugTestResult href "../DrugTestResult/"
      MedicalHealth <|-- Health
        click Health href "../Health/"
      MedicalHealth <|-- HealthHistory
        click HealthHistory href "../HealthHistory/"
      MedicalHealth <|-- HealthRecord
        click HealthRecord href "../HealthRecord/"
      MedicalHealth <|-- Prescription
        click Prescription href "../Prescription/"
      

      
```





## Inheritance
* **MedicalHealth** [ [External](External.md)]
    * [BloodType](BloodType.md)
    * [DNACode](DNACode.md)
    * [Disability](Disability.md)
    * [DrugTestResult](DrugTestResult.md)
    * [Health](Health.md)
    * [HealthHistory](HealthHistory.md)
    * [HealthRecord](HealthRecord.md)
    * [Prescription](Prescription.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:MedicalHealth](https://w3id.org/lmodel/dpv/pd/MedicalHealth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Medical Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#MedicalHealth |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:MedicalHealth |
| native | pd:MedicalHealth |
| exact | dpv_pd:MedicalHealth, dpv_pd_owl:MedicalHealth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MedicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MedicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health, medical conditions or health care
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Medical Health
exact_mappings:
- dpv_pd:MedicalHealth
- dpv_pd_owl:MedicalHealth
mixins:
- External
class_uri: pd:MedicalHealth

```
</details>

### Induced

<details>
```yaml
name: MedicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#MedicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health, medical conditions or health care
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Medical Health
exact_mappings:
- dpv_pd:MedicalHealth
- dpv_pd_owl:MedicalHealth
mixins:
- External
class_uri: pd:MedicalHealth

```
</details></div>