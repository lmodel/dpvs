---
search:
  boost: 10.0
---

# Class: Genetic 


_Information about inherited or acquired genetic characteristics_



<div data-search-exclude markdown="1">



URI: [pd:Genetic](https://w3id.org/lmodel/dpv/pd/Genetic)





```mermaid
 classDiagram
    class Genetic
    click Genetic href "../Genetic/"
      Health <|-- Genetic
        click Health href "../Health/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * [Health](Health.md)
        * **Genetic**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Genetic](https://w3id.org/lmodel/dpv/pd/Genetic) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Genetic




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Genetic |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Genetic |
| native | pd:Genetic |
| exact | dpv_pd:Genetic, dpv_pd_owl:Genetic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Genetic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Genetic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about inherited or acquired genetic characteristics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Genetic
exact_mappings:
- dpv_pd:Genetic
- dpv_pd_owl:Genetic
is_a: Health
class_uri: pd:Genetic

```
</details>

### Induced

<details>
```yaml
name: Genetic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Genetic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about inherited or acquired genetic characteristics
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Genetic
exact_mappings:
- dpv_pd:Genetic
- dpv_pd_owl:Genetic
is_a: Health
class_uri: pd:Genetic

```
</details></div>