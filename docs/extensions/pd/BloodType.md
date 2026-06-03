---
search:
  boost: 10.0
---

# Class: BloodType 


_Information about blood type_



<div data-search-exclude markdown="1">



URI: [pd:BloodType](https://w3id.org/lmodel/dpv/pd/BloodType)





```mermaid
 classDiagram
    class BloodType
    click BloodType href "../BloodType/"
      MedicalHealth <|-- BloodType
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **BloodType**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BloodType](https://w3id.org/lmodel/dpv/pd/BloodType) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Blood Type




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BloodType |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BloodType |
| native | pd:BloodType |
| exact | dpv_pd:BloodType, dpv_pd_owl:BloodType |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BloodType
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BloodType
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about blood type
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Blood Type
exact_mappings:
- dpv_pd:BloodType
- dpv_pd_owl:BloodType
is_a: MedicalHealth
class_uri: pd:BloodType

```
</details>

### Induced

<details>
```yaml
name: BloodType
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BloodType
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about blood type
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Blood Type
exact_mappings:
- dpv_pd:BloodType
- dpv_pd_owl:BloodType
is_a: MedicalHealth
class_uri: pd:BloodType

```
</details></div>