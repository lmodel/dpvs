---
search:
  boost: 10.0
---

# Class: FacialPrint 


_Information about facial print or pattern_



<div data-search-exclude markdown="1">



URI: [pd:FacialPrint](https://w3id.org/lmodel/dpv/pd/FacialPrint)





```mermaid
 classDiagram
    class FacialPrint
    click FacialPrint href "../FacialPrint/"
      Biometric <|-- FacialPrint
        click Biometric href "../Biometric/"
      
      
```





## Inheritance
* [Biometric](Biometric.md) [ [Identifying](Identifying.md)]
    * **FacialPrint**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FacialPrint](https://w3id.org/lmodel/dpv/pd/FacialPrint) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Facial Print




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FacialPrint |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FacialPrint |
| native | pd:FacialPrint |
| exact | dpv_pd:FacialPrint, dpv_pd_owl:FacialPrint |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FacialPrint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FacialPrint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about facial print or pattern
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Facial Print
exact_mappings:
- dpv_pd:FacialPrint
- dpv_pd_owl:FacialPrint
is_a: Biometric
class_uri: pd:FacialPrint

```
</details>

### Induced

<details>
```yaml
name: FacialPrint
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FacialPrint
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about facial print or pattern
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Facial Print
exact_mappings:
- dpv_pd:FacialPrint
- dpv_pd_owl:FacialPrint
is_a: Biometric
class_uri: pd:FacialPrint

```
</details></div>