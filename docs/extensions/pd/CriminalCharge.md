---
search:
  boost: 10.0
---

# Class: CriminalCharge 


_Information about criminal charges_



<div data-search-exclude markdown="1">



URI: [pd:CriminalCharge](https://w3id.org/lmodel/dpv/pd/CriminalCharge)





```mermaid
 classDiagram
    class CriminalCharge
    click CriminalCharge href "../CriminalCharge/"
      Criminal <|-- CriminalCharge
        click Criminal href "../Criminal/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Criminal](Criminal.md)
        * **CriminalCharge**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CriminalCharge](https://w3id.org/lmodel/dpv/pd/CriminalCharge) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Criminal Charge




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CriminalCharge |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CriminalCharge |
| native | pd:CriminalCharge |
| exact | dpv_pd:CriminalCharge, dpv_pd_owl:CriminalCharge |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CriminalCharge
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalCharge
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal charges
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Charge
exact_mappings:
- dpv_pd:CriminalCharge
- dpv_pd_owl:CriminalCharge
is_a: Criminal
class_uri: pd:CriminalCharge

```
</details>

### Induced

<details>
```yaml
name: CriminalCharge
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CriminalCharge
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about criminal charges
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal Charge
exact_mappings:
- dpv_pd:CriminalCharge
- dpv_pd_owl:CriminalCharge
is_a: Criminal
class_uri: pd:CriminalCharge

```
</details></div>