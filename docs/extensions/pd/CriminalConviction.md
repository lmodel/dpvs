---
search:
  boost: 10.0
---

# Class: CriminalConviction 


_Information about criminal convictions_



<div data-search-exclude markdown="1">



URI: [pd:CriminalConviction](https://w3id.org/lmodel/dpv/pd/CriminalConviction)





```mermaid
 classDiagram
    class CriminalConviction
    click CriminalConviction href "../CriminalConviction/"
      Criminal <|-- CriminalConviction
        click Criminal href "../Criminal/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Criminal](Criminal.md)
        * **CriminalConviction**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CriminalConviction](https://w3id.org/lmodel/dpv/pd/CriminalConviction) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Criminal Conviction




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CriminalConviction |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CriminalConviction |
| native | pd:CriminalConviction |
| exact | dpv_pd:CriminalConviction, dpv_pd_owl:CriminalConviction |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriminalConviction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalConviction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal convictions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Conviction
exact_mappings:
- dpv_pd:CriminalConviction
- dpv_pd_owl:CriminalConviction
is_a: Criminal
class_uri: pd:CriminalConviction

```
</details>

### Induced

<details>
```yaml
name: CriminalConviction
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalConviction
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal convictions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Conviction
exact_mappings:
- dpv_pd:CriminalConviction
- dpv_pd_owl:CriminalConviction
is_a: Criminal
class_uri: pd:CriminalConviction

```
</details></div>