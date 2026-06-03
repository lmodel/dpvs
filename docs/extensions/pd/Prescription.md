---
search:
  boost: 10.0
---

# Class: Prescription 


_Information about medical and pharmaceutical prescriptions_



<div data-search-exclude markdown="1">



URI: [pd:Prescription](https://w3id.org/lmodel/dpv/pd/Prescription)





```mermaid
 classDiagram
    class Prescription
    click Prescription href "../Prescription/"
      MedicalHealth <|-- Prescription
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **Prescription**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Prescription](https://w3id.org/lmodel/dpv/pd/Prescription) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Prescription




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Prescription |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Prescription |
| native | pd:Prescription |
| exact | dpv_pd:Prescription, dpv_pd_owl:Prescription |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Prescription
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Prescription
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about medical and pharmaceutical prescriptions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Prescription
exact_mappings:
- dpv_pd:Prescription
- dpv_pd_owl:Prescription
is_a: MedicalHealth
class_uri: pd:Prescription

```
</details>

### Induced

<details>
```yaml
name: Prescription
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Prescription
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about medical and pharmaceutical prescriptions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Prescription
exact_mappings:
- dpv_pd:Prescription
- dpv_pd_owl:Prescription
is_a: MedicalHealth
class_uri: pd:Prescription

```
</details></div>