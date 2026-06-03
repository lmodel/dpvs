---
search:
  boost: 10.0
---

# Class: FinancialStatus 


_Information about financial status or standing_



<div data-search-exclude markdown="1">



URI: [pd:FinancialStatus](https://w3id.org/lmodel/dpv/pd/FinancialStatus)





```mermaid
 classDiagram
    class FinancialStatus
    click FinancialStatus href "../FinancialStatus/"
      Financial <|-- FinancialStatus
        click Financial href "../Financial/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * **FinancialStatus**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FinancialStatus](https://w3id.org/lmodel/dpv/pd/FinancialStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Financial Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FinancialStatus |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FinancialStatus |
| native | pd:FinancialStatus |
| exact | dpv_pd:FinancialStatus, dpv_pd_owl:FinancialStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FinancialStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial status or standing
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Status
exact_mappings:
- dpv_pd:FinancialStatus
- dpv_pd_owl:FinancialStatus
is_a: Financial
class_uri: pd:FinancialStatus

```
</details>

### Induced

<details>
```yaml
name: FinancialStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FinancialStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about financial status or standing
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Financial Status
exact_mappings:
- dpv_pd:FinancialStatus
- dpv_pd_owl:FinancialStatus
is_a: Financial
class_uri: pd:FinancialStatus

```
</details></div>