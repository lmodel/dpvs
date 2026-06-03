---
search:
  boost: 10.0
---

# Class: Retina 


_Information about retina and the retinal patterns_



<div data-search-exclude markdown="1">



URI: [pd:Retina](https://w3id.org/lmodel/dpv/pd/Retina)





```mermaid
 classDiagram
    class Retina
    click Retina href "../Retina/"
      Biometric <|-- Retina
        click Biometric href "../Biometric/"
      
      
```





## Inheritance
* [Biometric](Biometric.md) [ [Identifying](Identifying.md)]
    * **Retina**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Retina](https://w3id.org/lmodel/dpv/pd/Retina) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Retina




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Retina |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Retina |
| native | pd:Retina |
| exact | dpv_pd:Retina, dpv_pd_owl:Retina |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Retina
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Retina
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about retina and the retinal patterns
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Retina
exact_mappings:
- dpv_pd:Retina
- dpv_pd_owl:Retina
is_a: Biometric
class_uri: pd:Retina

```
</details>

### Induced

<details>
```yaml
name: Retina
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Retina
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about retina and the retinal patterns
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Retina
exact_mappings:
- dpv_pd:Retina
- dpv_pd_owl:Retina
is_a: Biometric
class_uri: pd:Retina

```
</details></div>