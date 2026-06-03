---
search:
  boost: 10.0
---

# Class: FacialExpression 


_Information about facial expression_



<div data-search-exclude markdown="1">



URI: [pd:FacialExpression](https://w3id.org/lmodel/dpv/pd/FacialExpression)





```mermaid
 classDiagram
    class FacialExpression
    click FacialExpression href "../FacialExpression/"
      Biometric <|-- FacialExpression
        click Biometric href "../Biometric/"
      
      
```





## Inheritance
* [Biometric](Biometric.md) [ [Identifying](Identifying.md)]
    * **FacialExpression**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FacialExpression](https://w3id.org/lmodel/dpv/pd/FacialExpression) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Facial Expression




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FacialExpression |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FacialExpression |
| native | pd:FacialExpression |
| exact | dpv_pd:FacialExpression, dpv_pd_owl:FacialExpression |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FacialExpression
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FacialExpression
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about facial expression
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Facial Expression
exact_mappings:
- dpv_pd:FacialExpression
- dpv_pd_owl:FacialExpression
is_a: Biometric
class_uri: pd:FacialExpression

```
</details>

### Induced

<details>
```yaml
name: FacialExpression
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FacialExpression
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about facial expression
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Facial Expression
exact_mappings:
- dpv_pd:FacialExpression
- dpv_pd_owl:FacialExpression
is_a: Biometric
class_uri: pd:FacialExpression

```
</details></div>