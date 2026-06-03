---
search:
  boost: 10.0
---

# Class: Insurance 


_Information about Insurance_



<div data-search-exclude markdown="1">



URI: [pd:Insurance](https://w3id.org/lmodel/dpv/pd/Insurance)





```mermaid
 classDiagram
    class Insurance
    click Insurance href "../Insurance/"
      Financial <|-- Insurance
        click Financial href "../Financial/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * **Insurance**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Insurance](https://w3id.org/lmodel/dpv/pd/Insurance) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Insurance




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Insurance |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Insurance |
| native | pd:Insurance |
| exact | dpv_pd:Insurance, dpv_pd_owl:Insurance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Insurance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Insurance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about Insurance
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Insurance
exact_mappings:
- dpv_pd:Insurance
- dpv_pd_owl:Insurance
is_a: Financial
class_uri: pd:Insurance

```
</details>

### Induced

<details>
```yaml
name: Insurance
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Insurance
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about Insurance
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Insurance
exact_mappings:
- dpv_pd:Insurance
- dpv_pd_owl:Insurance
is_a: Financial
class_uri: pd:Insurance

```
</details></div>