---
search:
  boost: 10.0
---

# Class: Disability 


_Information about disabilities_



<div data-search-exclude markdown="1">



URI: [pd:Disability](https://w3id.org/lmodel/dpv/pd/Disability)





```mermaid
 classDiagram
    class Disability
    click Disability href "../Disability/"
      MedicalHealth <|-- Disability
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **Disability**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Disability](https://w3id.org/lmodel/dpv/pd/Disability) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Disability




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Disability |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Disability |
| native | pd:Disability |
| exact | dpv_pd:Disability, dpv_pd_owl:Disability |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Disability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Disability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about disabilities
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Disability
exact_mappings:
- dpv_pd:Disability
- dpv_pd_owl:Disability
is_a: MedicalHealth
class_uri: pd:Disability

```
</details>

### Induced

<details>
```yaml
name: Disability
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Disability
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about disabilities
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Disability
exact_mappings:
- dpv_pd:Disability
- dpv_pd_owl:Disability
is_a: MedicalHealth
class_uri: pd:Disability

```
</details></div>